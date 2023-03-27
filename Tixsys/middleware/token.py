from flask import request
from flask_jwt_extended import verify_jwt_in_request

def verify_bearer():
    if request.endpoint not in ('bp.login_user', 'bp.register_user'):
        verify_jwt_in_request()

def refresh_access():
    #Next update
    pass