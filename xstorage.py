#!env python

import os
import time
import hashlib
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import send_from_directory
from flask import jsonify
from flask import g
from werkzeug import utils

# Initialize the Flask application
app = Flask(__name__)
app.config.from_pyfile('config.py')


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def prepare_file(filename):
    s = '-'
    hashname = hashlib.md5(s.join((str(time.time()), filename.encode("utf-8")))).hexdigest()
    # os.path.splitext[1]
    ext = filename.rsplit('.', 1)[1]

    newfilename = '.'.join((hashname, ext))

    if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], hashname[0])):
        os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], hashname[0]))
    if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], hashname[0], hashname[1])):
        os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], hashname[0], hashname[1]))

    return newfilename


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    postfile = request.files['file']

    # Check if the file is one of the allowed types/extensions
    if postfile and allowed_file(postfile.filename):
        # Make the filename safe, remove unsupported chars
        filename = utils.secure_filename(postfile.filename)
        new_filename = prepare_file(postfile.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        postfile.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename[0], new_filename[1], new_filename))

        if 'json' in request.args:
            if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], new_filename[0], new_filename[1], new_filename)):
                return jsonify(status='error')
            return jsonify(status='success', fileurl="/".join(('uploads', new_filename[0], new_filename[1], new_filename)))
        else:
            if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], new_filename[0], new_filename[1], new_filename)):
                # Redirect the user to the uploaded_file route, which
                # will basicaly show on the browser the uploaded file
                return redirect(url_for('preview_file', filename=new_filename))
            return redirect(url_for('upload_file_fail'))
    else:
        return redirect(url_for('upload_error'))


@app.route('/upload_error')
def upload_error():
    return render_template('upload_error.html')


@app.route('/preview/')
def preview_index():
    return redirect(url_for('index'))


@app.route('/preview/<filename>')
def preview_file(filename):
    # todo: check exists file
    major = filename[0]
    minor = filename[1]
    ext = filename.rsplit('.', 1)[1]
    fileurl = "/".join(('uploads', major, minor, filename))
    print fileurl
    return render_template('preview.html', fileurl=fileurl, ext=ext)


# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<major>/<minor>/<filename>')
def uploaded_file(major, minor, filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], os.path.join(major, minor, filename))


if __name__ == '__main__':
    app.run()