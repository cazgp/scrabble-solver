from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Anagram(Base):
    __tablename__ = "anagrams"
    id = Column(Integer, primary_key=True)
    sorted = Column(String)
    words = Column(String)
    length = Column(Integer)
    a = Column(Integer)
    b = Column(Integer)
    c = Column(Integer)
    d = Column(Integer)
    e = Column(Integer)
    f = Column(Integer)
    g = Column(Integer)
    h = Column(Integer)
    i = Column(Integer)
    j = Column(Integer)
    k = Column(Integer)
    l = Column(Integer)
    m = Column(Integer)
    n = Column(Integer)
    o = Column(Integer)
    p = Column(Integer)
    q = Column(Integer)
    r = Column(Integer)
    s = Column(Integer)
    t = Column(Integer)
    u = Column(Integer)
    v = Column(Integer)
    w = Column(Integer)
    x = Column(Integer)
    y = Column(Integer)
    z = Column(Integer)


class Word(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True)
    word = Column(String)
    definition = Column(String)
    length = Column(Integer)


def get_session():
    engine = create_engine('sqlite:///words.db')
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    return session()
