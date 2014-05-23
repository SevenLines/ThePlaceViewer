from PySide.QtGui import QWidget
from PySide.QtGui import QRegion
from PySide.QtCore import QModelIndex, QPoint
from PySide.QtGui import QItemDelegate, QStyledItemDelegate
from PySide.QtGui import QPainter
from PySide.QtGui import QApplication
from PySide.QtCore import Qt
from gui.celebItemWidget import CelebItemWidget


class CelebItemDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        assert isinstance(painter, QPainter)
        assert isinstance(index, QModelIndex)

        device = painter.device()

        widget = CelebItemWidget()
        widget.set_celeb(index.data(Qt.EditRole))
        # widget.setGeometry(option.rect)
        widget.render(painter, QPoint(option.rect.x(), option.rect.y()),
                      QRegion(),QWidget.DrawChildren)

    # def sizeHint(self, option, index):
    #     assert isinstance(index, QModelIndex)
        # option.rect =



