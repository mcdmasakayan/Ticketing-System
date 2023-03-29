import os
from model.init_db import url
from datetime import timedelta


SECRET_KEY = 'hirayamnl'

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = url

SQLALCHEMY_TRACK_MODIFICATIONS = False

JSON_SORT_KEYS = False

JWT_COOKIE_SECURE = False

JWT_TOKEN_LOCATION = 'cookies'

JWT_SECRET_KEY = 'hirayamnl'

JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)