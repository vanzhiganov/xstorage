# xStorage

API Documentation: https://documenter.getpostman.com/view/607407/Uyr4KKsu

## Using libraries

See requirements.txt or setup.py file.

## Install

Create ${HOME}/xstorageserver.ini with settings:

```
[APP]
DEBUG = False
UPLOAD_FOLDER = /home/xstorage/UPLOAD
```

Nginx


uWSGI


Supervisor


## Docker

Build base image

    docker build -t xstorage-base -f Dockerfile .

Build app image

    docker build -t xstorage-app -f Dockerfile-app .

### Docker Compose

```yml
version: '3'
services:
  app:
    image: vanzhiganov/xstorage-app:0.2.0
    ports:
        - "8080:8080"
    volumes:
        - ./extra/xstorageserver.ini:/etc/xstorage/config.ini
        - ./extra/uwsgi.ini:/source/extra/uwsgi.ini
        - ./tmp/UPLOAD:/data
```