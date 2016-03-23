# coding=utf-8
from form_new import NewBlogEntryForm


def test_home_view(dbtransaction, new_entry, dummy_get_request):
    """Test that '/' returns a Query of Entries."""
    from journalapp.views import home
    response_dict = home(dummy_get_request)
    entries = response_dict['blog_posts']
    assert entries[0] == new_entry


def test_detail_view(dbtransaction, new_entry, dummy_get_request):
    """Test that detail_view returns the correct Entry page."""
    from journalapp.views import detail
    dummy_get_request.matchdict = {'entry_id': new_entry.id}
    response_dict = detail(dummy_get_request)
    assert response_dict['post'] == new_entry


def test_new_view(dbtransaction, dummy_get_request):
    """Test that the add_view returns a dict containing the proper form."""
    from journalapp.views import new
    response_dict = new(dummy_get_request)
    form = response_dict.get('form', None)
    assert isinstance(form, NewBlogEntryForm)


def test_edit_view(dbtransaction, new_entry, dummy_get_request):
    """Test that the add view returns a dict containing the proper form."""
    from journalapp.views import edit
    dummy_get_request.matchdict = {'entry_id': new_entry.id}
    response_dict = edit(dummy_get_request)
    print(response_dict)
    form = response_dict.get('form', None)
    print(form)
    assert isinstance(form, NewBlogEntryForm)


def test_edit_view_post(dbtransaction, new_entry, dummy_post_request):
    """Test that the add view returns a dict containing the proper form."""
    from journalapp.views import edit
    entry_id = new_entry.id
    dummy_post_request.path = '/edit'
    dummy_post_request.matchdict = {'entry_id': entry_id}
    response = edit(dummy_post_request)
    assert response.status_code == 302 and response.title == 'Found'
    loc_parts = response.location.split('/')
    assert loc_parts[-2] == 'detail' and int(loc_parts[-1]) == entry_id


def test_add_view_post(dbtransaction, dummy_post_request):
    """Test that the add_view returns a dict containing the proper form."""
    from journalapp.views import new
    dummy_post_request.path = '/add'
    response = new(dummy_post_request)
    assert response.status_code == 302 and response.title == 'Found'
    loc_parts = response.location.split('/')
    assert loc_parts[-2] == 'detail' and loc_parts[-1].isdigit()


def test_add_view_dupe(dbtransaction, dummy_post_request):
    """Test that the add_view returns a dict containing the proper form."""
    from journalapp.views import new
    dummy_post_request.path = '/add'
    response1 = new(dummy_post_request)
    assert response1.status_code == 302 and response1.title == 'Found'
    response2 = new(dummy_post_request)
    assert isinstance(response2, dict) and response2['form'].title.errors


def test_detail_error(dbtransaction, dummy_get_request):
    """Test that detail page gives a 404 when entry ID does not exist."""
    from journalapp.views import detail
    dummy_get_request.matchdict = {'pkey': 9999}
    response = detail(dummy_get_request)
    assert response.status_code == 404


def test_edit_error(dbtransaction, dummy_get_request):
    """Test that edit page gives a 404 when entry ID does not exist."""
    from journalapp.views import edit
    dummy_get_request.matchdict = {'pkey': 9999}
    response = edit(dummy_get_request)
    assert response.status_code == 404
