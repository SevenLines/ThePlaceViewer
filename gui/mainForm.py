#coding:utf-8
from Queue import Queue
from collections import defaultdict
from threading import Thread
import threading
import yaml
import shutil

from PySide.QtCore import QRect
from PySide.QtCore import QModelIndex, Signal
from PySide.QtCore import Qt, QByteArray
from PySide.QtCore import QEvent
from PySide.QtGui import QMainWindow, QSortFilterProxyModel, QPixmap

from core.siteparser import *
from gui.LabelImage import LabelImage
from gui.processInfoWidget import ProcessInfoWidget
from gui.ui.mainForm_ui import Ui_MainWindow
from models.celebritymodel import CelebrityModel
from core.config import *


logging.basicConfig()
log = logging.getLogger(__name__)


class ThreadCancel(Thread):
    _cancel = False
    queue = Queue()

    def cancel(self):
        self._cancel = True

    def is_canceled(self):
        return self._cancel


class MainForm(QMainWindow, Ui_MainWindow):
    # FIELDS
    model = CelebrityModel()
    SETTINGS_FILE = "config.yaml"
    log = logging.getLogger(__name__)
    last_thread = None
    images_count = 0
    last_image = None

    # SIGNALS
    pages_count_changed = Signal(int)
    image_added = Signal(int, ThePlaceImage, int)
    images_count_obtained = Signal(int)
    images_loaded = Signal()
    image_downloaded = Signal(QByteArray, ThePlaceImage)

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
        # self.lstImages.doubleClicked.connect(self.save_selected_image)
        self.lstImages.clicked.connect(self.image_selected)
        self.actionInvalideateCachePage.triggered.connect(self.invalidate_cache_page)
        self.actionInvalideateCacheCeleb.triggered.connect(self.invalidate_cache_celeb)
        self.image_downloaded.connect(self.show_image)
        self.image_added.connect(self.add_image)
        self.images_count_obtained.connect(self.resize_image_list_to_count)
        self.images_loaded.connect(self.resize_images_list)

        self.lstImages.installEventFilter(self)
        self.lblPreview.hide_icons = True

        self.load_ini()
        self.model.reset_data()

    def eventFilter(self, obj, event):
        assert isinstance(event, QEvent)
        if event.type() == QEvent.Resize:
            self.resize_images_list()
            return True
        return False
        # super(MainForm, self).eventFilter(*obj, **kwargs)


    def resize_image_list_to_count(self, count):
        """
        изменяет размеры таблицы изображений под кол-во картинок
        :param count: кол-во картинок
        """
        self.resize_images_list(as_empty=True, count=count)

    def invalidate_cache_page(self):
        """
        сбрасывает кеш текущей страницы с изображениями
        """
        celeb = self.get_selected_celeb()
        self.load_images(celeb, True)

    def invalidate_cache_celeb(self):
        """
        сбрасывает кеш для текущей знаменитости
        """
        celeb = self.get_selected_celeb()
        shutil.rmtree(os.path.join(icons_cache_dir, str(celeb.id)))
        self.load_images(celeb)

    def closeEvent(self, *args, **kwargs):
        if self.last_thread:
            self.last_thread.cancel()
        self.save_ini()

    def set_spnPage_maximum(self, count):
        """
        устанавливает макимально значение пагинатора
        :param count: максимальное значение
        """
        self.spnPage.setMaximum(count)
        self.spnPage.setSuffix("/ %s" % count)

    def resizeEvent(self, *args, **kwargs):
        super(MainForm, self).resizeEvent(*args, **kwargs)
        self.resize_images_list()

    def add_image(self, i, icon, count):
        """
        добавляет изображение в таблицу изображений
        :param i: порядковый номер изображения
        :param icon: изображение
        :param count: максимальное кол-во изображений
        """
        log.debug("%s %s %s" % (i, count, icon))
        label = LabelImage()
        label.setToolTip(icon.name)
        label.image = icon
        label.button_download_clicked.connect(label.setFocus)
        label.setAlignment(Qt.AlignCenter)

        row = i / columns_count
        col = i % columns_count

        self.lstImages.setCellWidget(row, col, label)

    def resize_images_list(self, as_empty=False, count=0):
        """
        изменяет размер таблицы изображений
        :param as_empty: если True то таблица будет перезаполнена с нуля
        :param count: максимальное кол-во ячеек в таблице
        """
        if as_empty:
            colsCount = self.lstImages.columnCount()
            rowsCount = self.lstImages.rowCount()
            # for x, y in product(xrange(colsCount), xrange(rowsCount)):
            #     widget = self.lstImages.cellWidget(y, x)
            #     self.lstImages.removeCellWidget(y, x)
            #     widget.setParent(None)//
            #     widget.deleteLater()
            #     del widget
            self.lstImages.clear()

            self.lstImages.setRowCount(count / columns_count)
            self.lstImages.setColumnCount(columns_count)
            self.lstImages.selectRow(0)
            self.lstImages.clearSelection()
            # self.lstImages.repaint()

        colsCount = self.lstImages.columnCount()
        rowsCount = self.lstImages.rowCount()

        if rowsCount == 0:
            return

        colsSize = self.lstImages.width() / colsCount \
                   - self.lstImages.verticalScrollBar().width() / colsCount

        for i in xrange(colsCount):
            self.lstImages.setColumnWidth(i, colsSize)
        for i in xrange(rowsCount):
            self.lstImages.setRowHeight(i, self.lstImages.height() / rows_count)

        # if as_empty:
        #     for x, y in product(xrange(colsCount), xrange(rowsCount)):
        #         self.lstImages.setCellWidget(y, x, LabelProcessAnimation())
        # QApplication.processEvents()
        log.debug("resized")

    def load_image(self, i, icon, count, invalidate):
        if not icon.is_cached or invalidate:
            icon.update_cached()
        self.image_added.emit(i, icon, count)

    def read_page(self, celeb, invalidate=False):
        """
        считывает информаци об изображениях со страницы
        :param celeb: знаменитость
        :param invalidate: если True изображения будут перскачены даже если содержаться в кеше
        """
        assert isinstance(celeb, Celeb)
        icons = get_icons(celeb, self.spnPage.value())

        thread = threading.current_thread()
        # print id(thread)
        first_time = True
        for i, (icon, count) in enumerate(icons):
            th = Thread(target=self.load_image, args=(i, icon, count, invalidate ))
            if thread.is_canceled():
                log.debug(u"%s thread has been canceled\n" % id(thread))
                log.debug("breaked")
                break
            if first_time:
                self.images_count_obtained.emit(count)
                first_time = False
            th.start()

        self.images_loaded.emit()
        print log.debug("thread end")

    def item_selected(self):
        """
        реакция на выбор знаменитости
        """
        # gc.collect()
        celeb = self.get_selected_celeb()
        assert isinstance(celeb, Celeb)
        self.lblCeleb.setText(celeb.full_name)
        self.obtain_pages_count(celeb)

        self.spnPage.setValue(1)
        self.load_images(celeb)

    def show_image(self, data, image):
        px = QPixmap()
        px.loadFromData(data)
        self.lblPreview.setPixmap(px)

    def download_image(self, image):
        b = image.full_image_bytes
        self.image_downloaded.emit(b, image)

    def image_selected(self):
        image = self.selected_image

        if self.last_image == image:
            return

        self.lblPreview.setPixmap(None)
        self.last_image = image

        thread = Thread(target=self.download_image, args=(image, ))
        thread.start()


    def get_selected_celeb(self):
        """
        возвращает выбранную знаменитость
        :return: Celeb
        """
        indexes = self.lstCelebs.selectedIndexes()
        if len(indexes) == 0:
            return None
        index = indexes[0]
        assert isinstance(index, QModelIndex)
        return index.data(Qt.EditRole)

    @property
    def selected_image(self):
        """
        Возвращает текущее выбранное изображение
        :return:
        """
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

    def save_image(self, image):
        b = image.full_image_bytes
        path = os.path.join(self.save_dir, image.celeb.full_name, image.name)
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        f = open(path, 'w')
        f.write(b)
        f.close()

    def save_selected_image(self):
        image = self.selected_image
        thread = ThreadCancel(target=self.save_image, args=(image, ))
        thread.start()

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
            'splitImagesState': self.splitImages.saveState(),
            'SelectedItem': self.get_selected_celeb().full_name if self.get_selected_celeb() else '',
            'SelectedPage': self.spnPage.value(),
        }

        f = open(self.SETTINGS_FILE, 'w')
        f.write(yaml.dump(s))
        f.close()

    def load_ini(self):
        try:
            s = yaml.load(open(self.SETTINGS_FILE))
        except IOError as e:
            return

        s['MainWindow'] = defaultdict(int, s['MainWindow'])
        self.restoreGeometry(s['MainWindow']['Geometry'] or None)
        self.splitImages.restoreState(s['MainWindow']['splitImagesState'] or None)
        # if 'SelectedItem' in s['MainWindow']:
        #     self.select_celeb(s['MainWindow']['SelectedItem'])
        #
        # if 'SelectedPage' in s['MainWindow']:
        #     self.spnPage.setValue(s['MainWindow']['SelectedPage'])

        self.edtFilter.setText(s['MainWindow']['Filter'] or '')
        self.update_filter()

    def select_celeb(self, full_name):
        assert isinstance(self.model, CelebrityModel)
        for row in xrange(self.model.rowCount()):
            index = self.model.index(0, row)
            assert isinstance(index, QModelIndex)
            s = index.data(Qt.DisplayRole)
            print s, full_name
            if s == full_name:
                print 'find'
                self.lstCeleb.setCurrentIndex(index)
                return



