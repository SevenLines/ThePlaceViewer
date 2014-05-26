import os

from PySide.QtGui import QDialog, QFileDialog
from core.config import config

from gui.ui.settings_dialog_ui import Ui_SettingsDialog


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.setupUi(self)

        self.btnSaveDirectory.clicked.connect(self.select_save_dir)

    def select_save_dir(self):
        directory = QFileDialog.getExistingDirectory(
            None,
            self.tr("Select save dir"),
            os.path.abspath(self.edtSaveDirectory.text()))

        if not directory:
            return

        if directory.startswith(os.path.abspath(os.curdir)):
            directory = os.path.relpath(directory, '.')
        self.edtSaveDirectory.setText(directory)

    def showEvent(self, *args, **kwargs):
        super(SettingsDialog, self).showEvent(*args, **kwargs)
        self.edtSaveDirectory.setText(config.save_dir)

    def accept(self, *args, **kwargs):
        super(SettingsDialog, self).accept(*args, **kwargs)
        config.save_dir = self.edtSaveDirectory.text()





