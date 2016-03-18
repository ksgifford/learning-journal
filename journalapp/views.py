# from pyramid.response import Response
from pyramid.view import view_config
from journalapp.models import query_table, query_post


@view_config(route_name='home', renderer='templates/blog_home.jinja2')
def home(request):
    all_posts = query_table()
    return dict(blog_posts=all_posts)


@view_config(route_name='detail', renderer='templates/blog_detail.jinja2')
def detail(request):
    pkey = request.matchdict.get("pkey")
    one_post = query_post(pkey)
    return dict(post=one_post)


# @view_config(route_name='new', renderer='templates/blog_new.jinja2')
# def detail():
#     pass


# @view_config(route_name='edit', renderer='templates/blog_nedit.jinja2')
# def detail(request):
#     pkey = request.matchdict.get("pkey")
#     one_post = query_post(pkey)
#     return dict(post=one_post)