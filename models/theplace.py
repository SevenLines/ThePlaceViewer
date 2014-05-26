import re
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
import sys
import core
from core.siteparser import *

Base = declarative_base()
engine = create_engine('sqlite:///theplace.db')


class Celeb(Base):
    __tablename__ = 'celebrity'

    id = Column(Integer, unique=True, primary_key=True)
    url = Column(String(200), nullable=False)
    full_name = Column(String(100), nullable=False, index=True)
    pages_count = Column(Integer, nullable=False, default=1)

    @staticmethod
    def from_url(url_link):
        u = url_link.split('@')
        m = re.search(u"photos/(.+)-mid(\d+).html", u[0])
        if not m:
            return
        c = Celeb()
        if u[1]:
            c.full_name = u[1]
        else:
            c.full_name = m.group(1).replace('_', ' ')
        c.id = int(m.group(2))
        c.url = u[0]
        return c

    def __repr__(self):
        return u'{id:>5}: {name} @:{url}'.format(
            id=self.id,
            name=self.full_name,
            url=self.url
        )

    def __str__(self):
        return self.__repr__()

    def __unicode__(self):
        return self.__repr__()

    @staticmethod
    def save_celebs_links_list_to_db(links_list):
        assert isinstance(links_list, list)
        if not len(links_list):
            return
        assert isinstance(links_list[0], unicode)

        session = sessionmaker(bind=engine)
        session = session()
        for c in links_list:
            celeb = Celeb.from_url(c)
            session.merge(celeb)
        session.commit()
        session.close()

    @staticmethod
    def fill_database():
        '''
        fill base with data abou Celebs
        '''
        # create session
        session = sessionmaker(engine)
        session = session()

        assert isinstance(session, Session)
        # get alphas urls
        urls = get_alphas_urls()
        for alpha_url in urls:
            print u"+-{0}".format(alpha_url)
            # get all celebs for alpha
            commit_freq = 5
            for i, c_url in enumerate(get_celebs_for_alpha(alpha_url)):
                #conver url to celeb
                celeb = Celeb.from_url(c_url)
                print u"|-\t{0}".format(celeb.full_name)
                # get pages count
                # celeb.pages_count = get_pages_count(celeb)
                session.merge(celeb)
                if i % commit_freq == 0:
                    session.commit()

        session.close()

    def get_page_url(self, page_num):
        return core.siteparser.get_page_url(self.id, page_num)

def create_database():
    try:
        Base.metadata.create_all(engine)
    except:
        log.error(sys.exc_info())

def main():
    argv = sys.argv
    if not len(argv):
        return

    if argv[1] == 'create':
        print "ready to create base structure"
        Base.metadata.create_all(engine)

    if argv[1] == 'fill':
        print "ready to fill base"
        Celeb.fill_database()
        print "fill complete"


if __name__ == '__main__':
    main()

