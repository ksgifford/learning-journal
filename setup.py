import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'markdown',
    'psycopg2',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'waitress',
    'wtforms',
    'zope.sqlalchemy',
    ]


tests_require = [
    'pytest',
    'pytest-watch',
    'tox',
    'webtest',
]

dev_requires = [
    'ipython',
    'pyramid-ipython',
]


setup(name='journalapp',
      version='0.0',
      description='journalapp',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='journalapp',
      install_requires=requires,
      extras_require={
        'test': tests_require,
        'dev': dev_requires,
      },
      entry_points=
      """
      [paste.app_factory]
      main = journalapp:main
      [console_scripts]
      initializedb = journalapp.scripts.initializedb:main
      """,
      )
