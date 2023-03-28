from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, verify_jwt_in_request
from flask_jwt_extended import set_access_cookies, set_refresh_cookies
from extensions import jwt

def verify_bearer():
    if request.endpoint not in ('bp.login_user', 'bp.register_user'):
        verify_jwt_in_request()

@jwt.expired_token_loader
def refresh_access(_, expired_token):
    expired_token_value = expired_token['sub']
    access_token = create_access_token(identity=expired_token_value)
    refresh_token = create_refresh_token(identity=expired_token_value)

    response = jsonify({'status':1,
                        'access_token':access_token})
    
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response

def revoke_access():
    print('logged_out')

    return True