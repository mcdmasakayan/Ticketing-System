from flask import Flask
from extensions import cors, migrate, session, jwt
from routes.blueprint import bp
from model.init_db import db
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
 
    jwt.init_app(app)
    session.init_app(app)
    cors.init_app(app)
    
    app.permanent_session_lifetime = timedelta(hours=24)
    
    with app.test_request_context():
        db.init_app(app)
        
    with app.app_context():
        db.create_all()
    
    return app

app = create_app()
app.register_blueprint(bp, url_prefix='/tixsys')
migrate.init_app(app, db)

if __name__ == '__main__':
    app.run()