import os
import time
import hashlib
from urllib.parse import urljoin
from flask import Blueprint, current_app, render_template, request, redirect, url_for, send_from_directory, jsonify

from werkzeug import utils
# import requests

hp = Blueprint('hp', __name__, template_folder='templates')


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']


def prepare_file(filename):
    s = '-'.join([str(time.time()), str(filename)])
    hashname = hashlib.md5(s.encode("utf-8")).hexdigest()
    # os.path.splitext[1]
    ext = filename.rsplit('.', 1)[1]

    newfilename = '.'.join((hashname, ext))

    if not os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], hashname[0])):
        os.mkdir(os.path.join(current_app.config['UPLOAD_FOLDER'], hashname[0]))
    if not os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], hashname[0], hashname[1])):
        os.mkdir(os.path.join(current_app.config['UPLOAD_FOLDER'], hashname[0], hashname[1]))

    return newfilename


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@hp.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@hp.route('/upload.html', methods=['POST'])
def upload():
    if 'file' not in request.files or request.files['file'].filename == '':
        return redirect(url_for('index'))

    # Get the name of the uploaded file
    postfile = request.files['file']

    # Check if the file is one of the allowed types/extensions
    # if not postfile and allowed_file(postfile.filename):
    #     return redirect(url_for('upload_error'))

    # Make the filename safe, remove unsupported chars
    filename = utils.secure_filename(postfile.filename)

    print(filename)

    # new_filename = prepare_file(postfile.filename)
    new_filename = prepare_file(postfile.filename)
    # Move the file form the temporal folder to
    # the upload folder we setup
    postfile.save(os.path.join(current_app.config['UPLOAD_FOLDER'], new_filename[0], new_filename[1], new_filename))

    if 'json' in request.args:
        if not os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], new_filename[0], new_filename[1], new_filename)):
            return jsonify(status='error')
        return jsonify(status='success', fileurl="/".join(('uploads', new_filename[0], new_filename[1], new_filename)))
    else:
        if os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], new_filename[0], new_filename[1], new_filename)):
            # Redirect the user to the uploaded_file route, which
            # will basicaly show on the browser the uploaded file
            return redirect(url_for('hp.preview_file', filename=new_filename))
        return redirect(url_for('hp.upload_file_fail'))


@hp.route('/upload_error.html')
def upload_error():
    return render_template('upload_error.html')


@hp.route('/preview/')
def preview_index():
    return redirect(url_for('hp.index'))


@hp.route('/preview/<filename>')
def preview_file(filename):
    # TODO: check exists file
    major = filename[0]
    minor = filename[1]
    ext = filename.rsplit('.', 1)[1]
    file_url = urljoin(current_app.config['URL'], "/".join(('uploads', major, minor, filename)))
    # print file_url
    return render_template('preview.html', fileurl=file_url, ext=ext)


# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@hp.route('/uploads/<major>/<minor>/<filename>')
def uploaded_file(major, minor, filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], os.path.join(major, minor, filename))
