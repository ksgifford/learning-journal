# from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy import desc
from .models import DBSession, Entry
import transaction


def query_table():
    return {'posts': DBSession.query(Entry).order_by(desc(Entry.created))}


def query_post(post_id):
    return {'posts': DBSession.query(Entry).filter(Entry.id == post_id)}


def new_entry(new_title=None, new_text=None):
    DBSession.add(Entry(title=new_title, text=new_text))
    DBSession.flush()
    transaction.commit()
    new_id = DBSession.query(Entry).order_by(desc(Entry.created))[0].id
    return new_id


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
