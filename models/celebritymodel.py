from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session
from threading import Thread

from PySide.QtCore import QAbstractListModel, QModelIndex, Qt, Signal

from models.theplace import Celeb, engine


class CelebrityModel(QAbstractListModel):
    # session = None
    celebs = []
    filter_string = ''
    cancel_loading = True
    current_thread = None

    data_obtained = Signal()

    def __init__(self, auto_connect=False, parent=None):
        QAbstractListModel.__init__(self, parent)
        if auto_connect:
            self.reset_data()

    def read_celebs(self):
        session = sessionmaker(bind=engine)
        session = session()
        assert isinstance(session, Session)
        self.celebs = []
        if session:
            self.beginResetModel()
            if self.filter_string:
                name = u'%{0}%'.format(self.filter_string);
                query = session.query(Celeb).filter(Celeb.full_name.like(name))
            else:
                query = session.query(Celeb)
            for c in query.order_by(Celeb.full_name).yield_per(5):
                if self.cancel_loading:
                    break
                self.celebs.append(c)

            self.endResetModel()
        session.close()
        self.data_obtained.emit()


    def reset_data(self):
        self.cancel_loading = True
        if self.current_thread:
            self.current_thread.join()
            current_thread = None
        self.cancel_loading = False

        thread = Thread(target=self.read_celebs)
        self.current_thread = thread
        thread.start()

    def set_filter(self, string):
        self.filter_string = string
        self.reset_data()

    def data(self, index, role):
        assert isinstance(index, QModelIndex)
        if role == Qt.DisplayRole:
            out = self.celebs[index.row()].full_name
            return out
        if role == Qt.EditRole:
            return self.celebs[index.row()]

    def rowCount(self, *args, **kwargs):
        return len(self.celebs)
