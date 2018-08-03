# coding: utf-8

from setuptools import setup

setup(
    name='xStorageServer',
    version='0.0.11',
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
        'Flask',
        'Flask-CDN',
        'Flask-Babel',
        'uwsgi',
    ],
)
