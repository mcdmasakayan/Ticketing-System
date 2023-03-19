from flask import request
from model.user.crud import verify_user, register_user, logout_user

def login_system():
    user_request = request.get_json()
    
    commands = {'login_user': (verify_user, 'POST'),
                'register_user': (register_user, 'POST')}
    
    if 'command' in user_request:
        action, method = commands.get(user_request['command'], (None, None))

        if action and request.method == method:
            return action()