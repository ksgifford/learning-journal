# from pyramid.response import Response
from pyramid.view import view_config

blog_posts = []

class BlogViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='templates/blog_home.jinja2')
    def home(self):
        return self.request.matchdict

    @view_config(route_name='detail', renderer='templates/blog_detail.jinja2')
    def detail(self):
        return self.request.matchdict
