from sqlalchemy import create_engine
from sqlalchemy.orm import create_session, Session, sessionmaker
from models.theplace import Celeb

engineOut = create_engine("sqlite:///theplace_old.db")
sessionOut = sessionmaker(bind=engineOut)
sessionOut = sessionOut()
assert isinstance(sessionOut, Session)

engineIn = create_engine("sqlite:///theplace.db")
sessionIn = sessionmaker(bind=engineIn)
sessionIn = sessionIn()
assert isinstance(sessionIn, Session)

for row in sessionOut.query(Celeb.full_name, Celeb.url, Celeb.id).all():
    c = Celeb()
    c.full_name = row.full_name
    c.url = row.url
    c.id = row.id
    # print(c)
    sessionIn.merge(c)
sessionIn.commit()



