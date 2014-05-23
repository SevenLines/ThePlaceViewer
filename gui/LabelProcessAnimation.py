from PySide.QtGui import QLabel, QMovie
from PySide.QtCore import Qt


class LabelProcessAnimation(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)

        self.setAlignment(Qt.AlignCenter)
        movie = QMovie("assets/load2.gif")
        self.setMovie(movie)
        movie.start()