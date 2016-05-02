# coding: utf-8

from setuptools import setup

setup(
    name='xStorageServer',
    version='0.0.10',
    author='Vyacheslav Anzhiganov',
    author_email='vanzhiganov@ya.ru',
    packages=[
        'xStorageServer',
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
        'Flask==0.10.1',
        'Flask-Babel==0.9',
        'Jinja2==2.8',
        'MarkupSafe==0.23',
        'Werkzeug==0.10.4',
        'itsdangerous==0.24',
        'wsgiref==0.1.2',
        'uwsgi',
    ],
)
