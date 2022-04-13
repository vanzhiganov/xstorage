import time
import hashlib
from urllib.parse import urlparse
import os
from urllib.parse import urljoin
from uuid import uuid1, uuid4
from flask import request, current_app, url_for
import jsonschema
import requests
from flask_restful import Resource
from xStorageServer.decorators import required_schema


class UploadByURLResource(Resource):
    @staticmethod
    def get_hash(link: str) -> str:
        return hashlib.md5(link.encode("utf-8")).hexdigest()

    @staticmethod
    def prepare_file(hashname: str, filename: str):
        ext = filename.rsplit('.', 1)[1]

        newfilename = '.'.join((hashname, ext))

        if not os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], hashname[0])):
            os.mkdir(os.path.join(current_app.config['UPLOAD_FOLDER'], hashname[0]))
        if not os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], hashname[0], hashname[1])):
            os.mkdir(os.path.join(current_app.config['UPLOAD_FOLDER'], hashname[0], hashname[1]))

        return newfilename

    def download_file(self, link):
        a = urlparse(link)

        hashname = self.get_hash(link)

        nfn = self.prepare_file(hashname, os.path.basename(a.path))
        local_filename = os.path.join(current_app.config['UPLOAD_FOLDER'], nfn[0], nfn[1], nfn)

        if os.path.exists(local_filename):
            return {
                "hash": hashname,
                "link": url_for('hp.uploaded_file', major=nfn[0], minor=nfn[1], filename=nfn)
            }
        
        # NOTE the stream=True parameter below
        with requests.get(link, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk:
                    f.write(chunk)
        return {
            "hash": hashname,
            "link": url_for('hp.uploaded_file', major=nfn[0], minor=nfn[1], filename=nfn)
        }


    @required_schema({
        "type": "object",
        "properties": {
            "link": {
                "type": "string"
            }
        },
        "requires": [
            "link"
        ]
    })
    def post(self) -> dict:
        link = request.json.get("link")
        link_details = self.download_file(link)
        return {
            "id": link_details['hash'],
            "link": urljoin(current_app.config['URL'], link_details['link'])
        }

class StatusResource(Resource):
    def get(self) -> dict:
        return {}