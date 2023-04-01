from flask import request, jsonify
from flask_jwt_extended import create_access_token, verify_jwt_in_request, jwt_required, get_jti
from flask_jwt_extended import set_access_cookies, unset_access_cookies, get_jwt, get_jwt_identity
from datetime import datetime, timedelta, timezone

blacklist = set()

def verify_bearer():
    if request.endpoint not in ('bp.login_user', 'bp.register_user'):
        jwt_required()
        verify_jwt_in_request()

        if get_jwt()['jti'] in blacklist:
            return jsonify({'status': 0,
                            'message':'Token is not valid.'})

def refresh_access(response):
    if request.endpoint not in ('bp.login_user', 'bp.register_user', 'bp.logout_user'):
        try:
            expiry = get_jwt()['exp']
            threshold = datetime.timestamp(datetime.now(timezone.utc) + timedelta(minutes=20))
 
            if threshold > expiry:
                access_token = create_access_token(identity=get_jwt_identity())

                response = jsonify({'status':1,
                                    'access_token':access_token})
                
                set_access_cookies(response, access_token)
            
        except (RuntimeError, KeyError):
            response = jsonify({'status':0,
                                'message':'Token is not valid.'})
    
    return response

def revoke_access():
    blacklist.add(get_jwt()['jti'])

    response = jsonify({'status':1,
                        'message':'User logged out.'})
    unset_access_cookies(response)
    
    return response