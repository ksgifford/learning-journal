# coding=utf-8

from journalapp.models import Entry, DBSession
from pyramid.testing import DummyRequest

import pytest


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

    # test_request.matchdict = {'title': create_entry.title}

    response = detail(test_request)
    post = response['post']
    assert post.title == create_entry.title


# def test_detail_view(dbtransaction, new_entry):
#     """Test that list_view returns a Query of Entries."""
#     test_request = DummyRequest()
#     test_request.matchdict = {'detail_id': new_entry.id}
#
#     response_dict = detail_view(test_request)
#     assert response_dict['entry'] == new_entry