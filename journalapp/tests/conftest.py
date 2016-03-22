# -*- coding: utf-8 -*-
import pytest
import os

from sqlalchemy import create_engine
from journalapp.models import DBSession, Base

# DATABASE_URL = 'postgresql+psycopg2://jackbot:@localhost:5432/'
DATABASE_URL = os.environ.get('JOURNAL_APP', None)


@pytest.fixture(scope='session')
def sqlengine(request):
    engine = create_engine(DATABASE_URL)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    def teardown():
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return engine


@pytest.fixture()
def dbtransaction(request, sqlengine):
    connection = sqlengine.connect()
    transaction = connection.begin()
    DBSession.configure(bind=connection)

    def teardown():
        transaction.rollback()
        connection.close()
        DBSession.remove()

    request.addfinalizer(teardown)
    return connection


@pytest.fixture()
def session(dbtransaction):
    from journalapp.models import DBSession
    return DBSession
