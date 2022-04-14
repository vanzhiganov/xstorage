import random
from flask import Flask
from flask_restful import Api


def init(**xargs):
    from xStorageServer.config import config

    # Initialize the Flask application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(random.random())
    app.config['DEBUG'] = config.getboolean('APP', 'DEBUG')
    app.config['UPLOAD_FOLDER'] = config.get('APP', 'UPLOAD_FOLDER')
    app.config['ALLOWED_EXTENSIONS'] = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm', 'flv', 'mp3']
    app.config['URL'] = config.get("APP", "URL")
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
