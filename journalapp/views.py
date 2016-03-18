# from pyramid.response import Response
from pyramid.view import view_config
from journalapp.models import query_table, query_post



class BlogViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='templates/blog_home.jinja2')
    def home(self):
        all_posts = query_table()
        return dict(blog_posts=all_posts)

    @view_config(route_name='detail', renderer='templates/blog_detail.jinja2')
    def detail(self):
        pkey = self.request.matchdict.get("pkey")
        one_post = query_post(pkey)
        return dict(post=one_post)
