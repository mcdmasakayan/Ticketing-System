from flask import request
from flask_jwt_extended import create_access_token, get_jwt_identity,verify_jwt_in_request

def verify_bearer():
    if request.endpoint not in ('bp.login_user', 'bp.register_user'):
        verify_jwt_in_request()

def refresh_access():
    identity = get_jwt_identity()
    create_access_token(identity=identity, fresh=False)

def revoke_access():
    #Todo
    pass