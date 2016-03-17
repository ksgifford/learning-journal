# from pyramid.response import Response
from pyramid.view import view_config
from journalapp.models import Entry

# blog_keys = [('ID', 'Title', 'Text', 'Date')]
blog_contents = Entry._query_table()

blog_posts = {}

for each in blog_contents:
    blog_posts.update(
        {each[0]: {
            "id": each[0],
            "title": each[1],
            "content": each[2],
            "posted": each[3]
            }
        }
    )


class BlogViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='templates/blog_home.jinja2')
    def home(self):
        return dict(blog_posts=blog_posts)

    @view_config(route_name='detail', renderer='templates/blog_detail.jinja2')
    def detail(self):
        pkey = self.request.matchdict.get("pkey")
        return dict(post=blog_posts[int(pkey)])
