from PySide.QtGui import QLabel, QMovie
from PySide.QtCore import Qt


class LabelProcessAnimation(QLabel):
    movie = None
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)

        self.setAlignment(Qt.AlignCenter)
        self.movie = QMovie("assets/load2.gif")
        self.setMovie(self.movie)
        # self.movie.start()

    def deleteLater(self, *args, **kwargs):
        # self.movie.stop()
        super(LabelProcessAnimation, self).deleteLater(*args, **kwargs)



