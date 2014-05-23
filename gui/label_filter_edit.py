
from PySide.QtCore import Qt
from PySide.QtGui import QLineEdit, QToolButton, QStyle, QIcon

class LabelFilterEdit(QLineEdit):

    clear_button = None

    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent)
        self.clear_button = QToolButton(self)
        self.clear_button.setText("clear")
        self.clear_button.hide()
        self.clear_button.clicked.connect(self.clear)
        # self.clear_button.setIcon(QIcon(":/denied.png"))

        self.textChanged.connect(self.update_clear_button)

    def resizeEvent(self, *args, **kwargs):
        super(LabelFilterEdit, self).resizeEvent(*args, **kwargs)

        sz = self.clear_button.sizeHint()
        frameWidth = 0 #self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)
        self.clear_button.move(self.rect().right() - sz.width() - frameWidth,
                               (self.rect().bottom() + 1 - sz.height()) / 2)

    def update_clear_button(self, text):
        self.clear_button.setVisible(len(text)>0)



