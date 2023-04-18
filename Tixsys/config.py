import os
from model.init_db import url
from datetime import timedelta

SECRET_KEY = 'hirayamnl'

BLUEPRINT_URL_PREFIX = '/tixsys'

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

THREADED = True

KEEP_ALIVE = 30

SQLALCHEMY_DATABASE_URI = url

SQLALCHEMY_TRACK_MODIFICATIONS = False

JSON_SORT_KEYS = False

JWT_COOKIE_SECURE = False

JWT_TOKEN_LOCATION = 'headers'

JWT_TOKEN_TYPE = 'Bearer'

JWT_SECRET_KEY = 'hirayamnl'

JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)

JWT_COOKIE_CSRF_PROTECT = False

CORS_ORIGINS = '/*'

CORS_SEND_WILDCARD = True

CORS_ALLOW_HEADERS = '*'

CORS_EXPOSE_HEADERS = '*'

CORS_SUPPORTS_CREDENTIALS = True