from PySide.QtGui import QWidget
from gui.ui.celeb_item_widget_ui import Ui_CelebItemWidget
from models.theplace import Celeb


class CelebItemWidget(QWidget, Ui_CelebItemWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Ui_CelebItemWidget.__init__(self, parent)
        self.setupUi(self)

    def set_celeb(self, celeb):
        # assert isinstance(celeb, Celeb)
        self.lblInfo.setText( celeb.full_name)