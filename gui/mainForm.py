from Queue import Queue
from threading import Thread
import threading
import yaml
from itertools import product

from PySide.QtCore import QRect
from PySide.QtCore import QModelIndex
from PySide.QtGui import QPixmap, QApplication
from PySide.QtCore import Qt
from PySide.QtGui import QMainWindow, QSortFilterProxyModel, QLabel

from core.siteparser import *
from gui.LabelProcessAnimation import LabelProcessAnimation
from gui.processInfoWidget import ProcessInfoWidget
from gui.ui.mainForm_ui import Ui_MainWindow
from models.celebritymodel import CelebrityModel


logging.basicConfig()

class ThreadCancel(Thread):
    _cancel = False
    queue = Queue()
    def cancel(self):
        self._cancel = True
    def is_canceled(self):
        return self._cancel


class MainForm(QMainWindow, Ui_MainWindow):
    proxy_model = QSortFilterProxyModel()
    model = CelebrityModel()
    SETTINGS_FILE = "config.yaml"
    log = logging.getLogger(__name__)
    processInfoWidget = None
    lastThread = None
    images_count = 0

    gui_thread = None
    queue = Queue()
    columns_count = 3
    rows_count = 3

    end = False

    def __init__(self, parent=None):
        Ui_MainWindow.__init__(self)
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.processInfoWidget = ProcessInfoWidget()

        self.lstCelebs.setModel(self.model)
        self.edtFilter.textChanged.connect(self.update_filter)

        self.model.modelReset.connect(self.end_load)
        self.lstCelebs.clicked.connect(self.item_selected)

        self.load_ini()
        self.model.reset_data()

    def closeEvent(self, *args, **kwargs):
        if self.lastThread:
            self.lastThread.cancel()
        self.save_ini()

    def set_images_count(self, count):
        self.images_count = count
        self.lstImages.clear()

    def resizeEvent(self, *args, **kwargs):
        super(MainForm, self).resizeEvent(*args, **kwargs)
        self.resize_images_list()


    def add_image(self, i, icon, count):
        with threading.Lock():
            label = QLabel()
            label.setPixmap(QPixmap(icon.icon_cache_path))
            label.setAlignment(Qt.AlignCenter)

            row = i / self.columns_count
            col = i % self.columns_count

            self.lstImages.setCellWidget(row, col, label)

    def resize_images_list(self, as_empty=False, count=0):
        with threading.Lock():
            if as_empty:
                self.lstImages.clear()
                self.lstImages.setRowCount(count / self.columns_count)
                self.lstImages.setColumnCount(self.columns_count)
                self.lstImages.update()

            colsCount = self.lstImages.columnCount()
            rowsCount = self.lstImages.rowCount()

            colsSize = self.lstImages.width() / colsCount \
                       - self.lstImages.verticalScrollBar().width() / colsCount

            for i in xrange(colsCount):
                self.lstImages.setColumnWidth(i, colsSize)
            for i in xrange(rowsCount):
                self.lstImages.setRowHeight(i, self.lstImages.height() / self.rows_count)

            if as_empty:
                for x, y in product(xrange(colsCount), xrange(rowsCount)):
                    self.lstImages.setCellWidget(y,x, LabelProcessAnimation())
            QApplication.processEvents()

    def read_page(self, celeb):
        page = celeb.get_page_url(1)
        icons = get_icons(page)

        thread = threading.current_thread()
        print id(thread)

        for i, (icon, count) in enumerate(icons):
            if thread.is_canceled():
                log.debug(u"%s thread has been canceled\n" % id(thread))
                print "breaked"
                break
            if not icon.is_cached:
                icon.update_cached()
            thread.queue.put((i, icon, count))
            thread.queue.join()

    def item_selected(self):
        if self.lastThread:
            self.lastThread.cancel()
            self.lastThread = None

        index = self.lstCelebs.selectedIndexes()[0]
        assert isinstance(index, QModelIndex)
        celeb = index.data(Qt.EditRole)

        thread = ThreadCancel(target=self.read_page, args=(celeb,))
        self.lastThread = thread
        thread.start()

        ffirst = True
        while thread.is_alive():
            if not thread.queue.empty():
                i, icon, count = thread.queue.get()
                if ffirst:
                    ffirst = False
                    self.lstImages.clear()
                    self.resize_images_list(as_empty=True, count=count)
                self.add_image(i, icon, count)
                thread.queue.task_done()
                if thread.is_canceled():
                    break
            QApplication.processEvents()

        self.resize_images_list()

    def begin_process(self):
        self.processInfoWidget.setParent(self.lstCelebs)
        self.processInfoWidget.setGeometry(
            QRect(0, 0, self.lstCelebs.width(), self.lstCelebs.height()))
        self.processInfoWidget.show()

    def end_load(self):
        self.lstCelebs.resizeColumnsToContents()
        # self.processInfoWidget.hide()

    def update_filter(self):
        text = self.edtFilter.text()
        self.model.set_filter(text)

    def save_ini(self):
        s = dict()
        s['MainWindow'] = {
            'Geometry': self.saveGeometry(),
            'Filter': self.edtFilter.text(),
        }

        f = open(self.SETTINGS_FILE, 'w')
        f.write(yaml.dump(s))
        f.close()

    def load_ini(self):
        try:
            s = yaml.load(open(self.SETTINGS_FILE))
        except IOError as e:
            return
        self.restoreGeometry(s['MainWindow']['Geometry'] or None)
        self.edtFilter.setText(s['MainWindow']['Filter'] or '')
        self.update_filter()
