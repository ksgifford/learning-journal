# coding=utf-8

from journalapp.models import Entry, DBSession


def test_create_entry(session):
    new_model = Entry(name="jill", value=42)
    assert new_model.id is None
    DBSession.add(new_model)
    DBSession.flush()
    assert new_model.id is not None
