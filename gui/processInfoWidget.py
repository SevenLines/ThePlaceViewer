from PySide.QtGui import QWidget
from gui.ui.process_info_widget_ui import Ui_ProcessInfoWidget


class ProcessInfoWidget(Ui_ProcessInfoWidget, QWidget):
    def __init__(self, parent=None):
        Ui_ProcessInfoWidget.__init__(self, parent)
        QWidget.__init__(self, parent)
        self.setupUi(self)
