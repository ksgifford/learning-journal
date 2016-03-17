import datetime
import psycopg2
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
    DateTime,
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Entry(Base):
    """Class for creating database blog entries."""
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(128), unique=True)
    text = Column(Unicode())
    created = Column(DateTime, default=datetime.datetime.utcnow)

    def _query_table():
        entry_list = []
        conn = psycopg2.connect(dbname="KSGifford", user="KSGifford")
        cur = conn.cursor()
        query = 'SELECT * FROM entries;'
        cur.execute(query)
        entry_list = cur.fetchall()
        return entry_list

Index('my_index', Entry.title, unique=True)
