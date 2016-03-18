# coding=utf-8

from journalapp.models import Entry, DBSession
from pyramid.view import view_config
from pyramid.testing import DummyRequest
import pytest


# @pytest.fixture()
# def app():
#     from journalapp import main
#     from webtest import TestApp
#     app = main()
#     return TestApp(app)


@pytest.fixture()
def create_entry(request):
    entry = Entry(title="Test Title", text="Test Text")
    DBSession.add(entry)
    DBSession.flush()
    return entry


def test_view_home(session, create_entry):
    from journalapp.views import home
    test_request = DummyRequest(path='/')

    response = home(test_request)
    posts = response['blog_posts']
    assert posts['posts'][0].title == create_entry.title


def test_view_detail(session, create_entry):
    from journalapp.views import detail
    test_request = DummyRequest(path='/entry/{pkey:\d+}')
    test_request.matchdict = {'title': create_entry.title}

    response = detail(test_request)
    post = response['post']
    assert post['posts'].title == create_entry.title
