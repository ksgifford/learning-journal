# coding=utf-8

from journalapp.models import MyModel, DBSession


def test_create_mymodel(Base):
    new_model = MyModel(name="jill", value=42)
    assert new_model.id is None
    DBSession.add(new_model)
    DBSession.flush()
    assert new_model.id is not None
