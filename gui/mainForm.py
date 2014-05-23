from Queue import Queue
from threading import Thread
import threading
import yaml
import shutil
from itertools import product

from PySide.QtCore import QRect
from PySide.QtCore import QModelIndex, Signal
from PySide.QtGui import QPixmap, QApplication
from PySide.QtCore import Qt
from PySide.QtGui import QMainWindow, QSortFilterProxyModel

from core.siteparser import *
from gui.LabelImage import LabelImage
from gui.LabelProcessAnimation import LabelProcessAnimation
from gui.processInfoWidget import ProcessInfoWidget
from gui.ui.mainForm_ui import Ui_MainWindow
from models.celebritymodel import CelebrityModel
from core.config import *

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
    last_thread = None
    images_count = 0

    gui_thread = None
    queue = Queue()
    columns_count = 3
    rows_count = 3
    save_dir = "output"

    end = False

    pages_count_changed = Signal(int)
    image_added = Signal(ThePlaceImage)

    def __init__(self, parent=None):
        Ui_MainWindow.__init__(self)
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.processInfoWidget = ProcessInfoWidget()

        self.lstCelebs.setModel(self.model)
        self.edtFilter.textChanged.connect(self.update_filter)

        self.model.modelReset.connect(self.end_load)
        self.lstCelebs.clicked.connect(self.item_selected)
        self.spnPage.valueChanged.connect(self.load_images_for_selected)
        self.pages_count_changed.connect(self.set_spnPage_maximum)
        self.lstImages.doubleClicked.connect(self.save_selected_image)
        self.actionInvalideateCachePage.triggered.connect(self.invalidate_cache_page)
        self.actionInvalideateCacheCeleb.triggered.connect(self.invalidate_cache_celeb)

        self.load_ini()
        self.model.reset_data()

    def invalidate_cache_page(self):
        celeb = self.get_selected_celeb()
        self.load_images(celeb, True)

    def invalidate_cache_celeb(self):
        celeb = self.get_selected_celeb()
        shutil.rmtree(os.path.join(icons_cache_dir, str(celeb.id)))
        self.load_images(celeb)

    def closeEvent(self, *args, **kwargs):
        if self.last_thread:
            self.last_thread.cancel()
        self.save_ini()

    def set_spnPage_maximum(self, count):
        self.spnPage.setMaximum(count)
        self.spnPage.setSuffix("/ %s" % count)

    def set_images_count(self, count):
        self.images_count = count
        self.lstImages.clear()

    def resizeEvent(self, *args, **kwargs):
        super(MainForm, self).resizeEvent(*args, **kwargs)
        self.resize_images_list()


    def add_image(self, i, icon, count):
        with threading.Lock():
            label = LabelImage()
            label.image = icon
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
                self.lstImages.selectRow(0)
                self.lstImages.clearSelection()
                self.lstImages.repaint()

            colsCount = self.lstImages.columnCount()
            rowsCount = self.lstImages.rowCount()

            if rowsCount == 0:
                return

            colsSize = self.lstImages.width() / colsCount \
                       - self.lstImages.verticalScrollBar().width() / colsCount

            for i in xrange(colsCount):
                self.lstImages.setColumnWidth(i, colsSize)
            for i in xrange(rowsCount):
                self.lstImages.setRowHeight(i, self.lstImages.height() / self.rows_count)

            if as_empty:
                for x, y in product(xrange(colsCount), xrange(rowsCount)):
                    self.lstImages.setCellWidget(y, x, LabelProcessAnimation())
            QApplication.processEvents()

    def read_page(self, celeb, invalidate=False):
        assert isinstance(celeb, Celeb)
        icons = get_icons(celeb, self.spnPage.value())

        thread = threading.current_thread()
        print id(thread)

        for i, (icon, count) in enumerate(icons):
            if thread.is_canceled():
                log.debug(u"%s thread has been canceled\n" % id(thread))
                print "breaked"
                break
            if not icon.is_cached or invalidate:
                icon.update_cached()
            self.image_added.emit(icon)
            thread.queue.put((i, icon, count))
            thread.queue.join()
        print "thread end"

    def item_selected(self):
        celeb = self.get_selected_celeb()

        self.obtain_pages_count(celeb)

        self.spnPage.setValue(1)
        self.load_images(celeb)

    def get_selected_celeb(self):
        indexes = self.lstCelebs.selectedIndexes()
        if len(indexes)==0:
            return None
        index = indexes[0]
        assert isinstance(index, QModelIndex)
        return index.data(Qt.EditRole)

    def get_selected_image(self):
        label = self.lstImages.cellWidget(self.lstImages.currentRow(),
                                          self.lstImages.currentColumn())
        assert isinstance(label, LabelImage)
        return label.image

    def load_images_for_selected(self):
        celeb = self.get_selected_celeb()
        self.load_images(celeb)

    def get_pages_info(self, celeb):
        count = get_pages_count(celeb)
        self.pages_count_changed.emit(count)

    def obtain_pages_count(self, celeb):
        thread = Thread(target=self.get_pages_info, args=(celeb, ))
        thread.start()

    def load_images(self, celeb, invalidate=False):
        if self.last_thread:
            self.last_thread.cancel()
            self.last_thread = None

        if not celeb:
            return

        thread = ThreadCancel(target=self.read_page, args=(celeb, invalidate))
        self.last_thread = thread
        thread.start()

        ffirst = True
        while thread.is_alive():
            if not thread.queue.empty():
                i, icon, count = thread.queue.get()
                if ffirst:
                    ffirst = False
                    self.resize_images_list(as_empty=True, count=count)
                self.add_image(i, icon, count)
                thread.queue.task_done()
                if thread.is_canceled():
                    break
            QApplication.processEvents()
        print "complete"
        self.resize_images_list()

    def save_image(self, image):
        b = image.full_image_bytes
        path = os.path.join(self.save_dir, image.celeb.full_name, image.name)
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        f = open(path, 'w')
        f.write(b)
        f.close()

    def save_selected_image(self):
        image = self.get_selected_image()
        thread = ThreadCancel(target=self.save_image, args=(image, ))
        thread.start()

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
