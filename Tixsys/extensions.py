from flask_cors import CORS
from flask_migrate import Migrate
from flask_sessionstore import Session
from flask_jwt_extended import JWTManager

cors = CORS()
migrate = Migrate()
session = Session()
jwt = JWTManager()