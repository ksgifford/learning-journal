from pyramid.config import Configurator
from sqlalchemy import engine_from_config

import os

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    database_url = os.environ.get('JOURNAL_APP', None)
    if database_url is not None:
        settings['sqlalchemy.url'] = database_url

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('detail', '/entry/{pkey:\d+}')
    config.add_route('new', '/new/')
    config.add_route('edit', '/edit/{pkey:\d+}')
    config.scan()
    return config.make_wsgi_app()
