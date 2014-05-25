from threading import Thread
import os

from PySide.QtGui import QLabel, QPixmap, QPushButton, QIcon, QMovie
from PySide.QtCore import Qt, Signal, QSize
from PySide.QtGui import QImageReader

from core.theplaceimage import ThePlaceImage
from core import config


class LabelImage(QLabel):
    _pixmap = None
    _image = None
    _hide_icons = False
    _icon_size = 28

    download_started = Signal()
    download_ended = Signal()
    button_download_clicked = Signal()

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.setText(self.tr("<u>can't obtain picture</u>"))

        self.lblLoadProcess = QLabel("...", self)
        self.lblLoadProcess.setMovie(QMovie(":/loading.gif"))
        self.lblLoadProcess.setAlignment(Qt.AlignCenter)
        self.lblLoadProcess.hide()

        self.btnDownload = QPushButton("", self)
        self.btnDownload.setIcon(QIcon(":/folder.png"))
        self.btnDownload.setIconSize(QSize(self._icon_size, self._icon_size))
        self.btnDownload.setFlat(True)
        self.btnDownload.clicked.connect(self.save_image)
        self.btnDownload.clicked.connect(self.button_download_clicked)

        self.download_ended.connect(self.check_image)
        self.download_ended.connect(self.lblLoadProcess.hide)
        self.download_ended.connect(self.btnDownload.show)
        self.download_ended.connect(self.end_load_anim)

        self.download_started.connect(self.start_load_anim)
        self.download_started.connect(self.btnDownload.hide)
        self.download_started.connect(self.lblLoadProcess.show)
        # self.destroyed.connect(self.on_destroyed)

    def start_load_anim(self):
        self.lblLoadProcess.movie().start()

    def end_load_anim(self):
        self.lblLoadProcess.movie().stop()

    @property
    def save_path(self):
        return os.path.join(config.save_dir, self._image.celeb.full_name, self._image.name)

    def save_image_thread_callback(self):
        self.download_started.emit()

        b = self._image.full_image_bytes
        path = self.save_path
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        f = open(path, 'w')
        f.write(b)
        f.close()

        self.download_ended.emit()

    def save_image(self):
        thread = Thread(target=self.save_image_thread_callback)
        thread.start()

    def check_image(self):
        if self._image:
            if os.path.exists(self.save_path):
                self.btnDownload.setIcon(QIcon(":/check.png"))
                return True
        self.btnDownload.setIcon(QIcon(":/folder.png"))
        return False

    def __setProp(self):
        if self._pixmap:
            QLabel.setPixmap(self, self._pixmap.scaled(
                self.width(), self.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            QLabel.setPixmap(self, QPixmap())

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        assert isinstance(image, ThePlaceImage)
        self._image = image
        path = os.path.abspath(image.icon_cache_path).replace('\\', '/')
        self.check_image()
        self.setPixmap(QPixmap(path))

    def setPixmap(self, px):
        self._pixmap = px
        self.__setProp()
        self.btnDownload.setVisible(not self.hide_icons and px is not None)

    def resizeEvent(self, *args, **kwargs):
        super(LabelImage, self).resizeEvent(*args, **kwargs)
        self.__setProp()

        self.btnDownload.move(self.width() - self.btnDownload.width() - 3,
                              self.height() - self.btnDownload.height() - 2)
        self.lblLoadProcess.setGeometry(self.btnDownload.geometry())

    @property
    def hide_icons(self):
        return self._hide_icons

    @hide_icons.setter
    def hide_icons(self, value):
        self._hide_icons = value
        self.btnDownload.setVisible(not self.hide_icons)



