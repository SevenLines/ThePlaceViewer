import sys

from PySide.QtGui import QApplication
from gui.mainForm import MainForm


def main():
    app = QApplication(sys.argv)

    if sys.platform == 'win32':
        app.addLibraryPath('win')

    frm = MainForm()
    frm.show()

    app.exec_()


if __name__ == "__main__":
    main()