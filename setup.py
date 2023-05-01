from setuptools import setup
from xStorageServer import __version__

setup(
    name='xStorageServer',
    version=__version__,
    author='Vyacheslav Anzhiganov',
    author_email='vanzhiganov@ya.ru',
    packages=[
        'xStorageServer',
        'xStorageServer.pages',
        'xStorageServer.resources'
    ],
    package_data={
        'xStorageServer': [
            'static/css/*.css',
            'static/fonts/*.*',
            'static/images/*.*',
            'static/js/*.js',
            'static/js/ie/*.js',
            'templates/*.html',
        ]
    },
    scripts=[
        'xstorage-server.py'
    ],
    install_requires=[
        'aniso8601==9.0.1',
        'attrs==21.4.0',
        'click==8.0.4',
        'Flask==2.3.2',
        'Flask-RESTful==0.3.9',
        'itsdangerous==2.0.1',
        'Jinja2==3.0.3',
        'jsonschema==4.0.0',
        'MarkupSafe==2.0.1',
        'pyrsistent==0.18.0',
        'pytz==2022.1',
        'requests==2.27.1',
        'six==1.16.0',
        'Werkzeug==2.0.3',
    ],
)
