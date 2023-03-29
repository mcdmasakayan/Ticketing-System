from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from uuid import uuid4
from werkzeug.security import check_password_hash
from model.init_db import db
from model.user.data import User

def authenticate_user(data, get_opened_entity):
    user = get_opened_entity(entity=User, email=data['email'], archived=False, select='first')
    
    if not user:
        user = get_opened_entity(entity=User, username=data['username'], archived=False, select='first')

    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.public_id)

        response = jsonify({'status':1,
                            'access_token':access_token})

        set_access_cookies(response, access_token)

        return response
        
    
    return jsonify({'status':0,
                    'message':'Username or Password is invalid.'})
    
    

def save_user(data, get_opened_entity):
    exist = get_opened_entity(entity=User, email=data['email'], archived=False, select='first')

    if not exist:
        exist = get_opened_entity(entity=User, username=data['username'], archived=False, select='first')

    if exist:
        return jsonify({'status':0,
                        'message':'Email or Username invalid.'})
    
    user = User(public_id=str(uuid4()), email=data['email'], username=data['username'], password=data['password'],
                first_name=data['first_name'], last_name=data['last_name'])
    
    db.session.add(user)
    db.session.commit()

    return jsonify({'status':1,
                    'message':f'{user.first_name} {user.last_name} registered as {user.username}.'})