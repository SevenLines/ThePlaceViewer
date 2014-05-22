from PySide.QtGui import QLabel, QPixmap
from PySide.QtCore import Qt

from core.image import Image


class LabelImage(QLabel):
    _pixmap = None
    _image = None

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.setText(self.tr("<u>can't obtain picture</u>"))

    def __setProp(self):
        if self._pixmap:
            QLabel.setPixmap(self, self._pixmap.scaled(
                self.width(), self.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        assert isinstance(image, Image)
        self._image = image
        self.setPixmap(QPixmap(image.icon_cache_path))

    def setPixmap(self, px):
        self._pixmap = px
        self.__setProp()

    def resizeEvent(self, *args, **kwargs):
        self.__setProp()
        super(LabelImage, self).resizeEvent(*args, **kwargs)



