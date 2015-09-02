DEBUG = True

SERVER_NAME = '127.0.0.1:5001'

SECRET_KEY = '123'

# for uploading
UPLOAD_FOLDER = '/storage'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm', 'flv', 'mp3']
MAX_CONTENT_LENGTH = 134217728

# for Babel
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'UTC'