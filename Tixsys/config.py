import os
from extensions import redis
from model.init_db import db, url
from datetime import timedelta


SECRET_KEY = 'hirayamnl'

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = url

SQLALCHEMY_TRACK_MODIFICATIONS = False

SESSION_PERMANENT = True

SESSION_TYPE = 'sqlalchemy'

SESSION_SQLALCHEMY = db

JSON_SORT_KEYS = False

JWT_SECRET_KEY = 'hirayamnl'

JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)

JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)