import os
import time
import hashlib
import random
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify, g
from flask_restful import Api
from flask_cdn import CDN
from werkzeug import utils


def init(**xargs):
    from xStorageServer.config import config

    # Initialize the Flask application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(random.random())
    app.config['DEBUG'] = config.getboolean('APP', 'DEBUG')
    app.config['UPLOAD_FOLDER'] = config.get('APP', 'UPLOAD_FOLDER')
    app.config['ALLOWED_EXTENSIONS'] = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm', 'flv', 'mp3']
    app.config['URL'] = config.get("APP", "URL")
    CDN(app)
    return app


def init_app(**xargs):
    from xStorageServer.pages import hp
    from xStorageServer.resources import UploadByURLResource, StatusResource
    app = init(**xargs)
    api = Api(app)
    # 
    api.add_resource(StatusResource, '/api/v1/status')
    api.add_resource(UploadByURLResource, '/api/v1/upload')
    # 
    app.register_blueprint(hp)

    return app


# def init_app(**xargs):
#     from xStorageServer.pages import hp
#     app = init(**xargs)
#     app.register_blueprint(hp)
#     return app


if __name__ == '__main__':
    app.run()
