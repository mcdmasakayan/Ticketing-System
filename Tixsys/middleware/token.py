import jwt
from flask import jsonify, request
from datetime import datetime, timedelta
from config import SECRET_KEY
 
def check_token():
    token = request.args.get('token')
    data = jwt.decode(token, SECRET_KEY)
    public_id = data['public_id']

    return public_id

def add_token(public_id):
    token = request.args.get('token')
    data = jwt.decode(token, SECRET_KEY)
    current_session_id = data['public_id']

    if current_session_id:

        if current_session_id != public_id:
            token = jwt.encode({
                'public_id': public_id,
                'exp' : datetime.utcnow() + timedelta(minutes = 30)
            }, SECRET_KEY) 
            
            return jsonify({'token' : token.decode('UTF-8')})
        
    else:
        token = jwt.encode({
            'public_id': public_id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, SECRET_KEY)
        
        return jsonify({'token' : token.decode('UTF-8')})

def clear_token():
    pass