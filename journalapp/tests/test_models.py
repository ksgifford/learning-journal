# coding=utf-8

from journalapp.models import Entry, DBSession


def test_create_entry(session):
    new_model = Entry(title="Blog Post", text="my entry goes here")
    assert new_model.id is None
    DBSession.add(new_model)
    DBSession.flush()
    assert new_model.id is not None
