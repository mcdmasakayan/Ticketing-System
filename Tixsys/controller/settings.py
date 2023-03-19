from flask import request
from model.settings.crud import archive_user

def settings_system(**kwargs):
    user_request = request.get_json()
    commands = {'archive_user': (archive_user, 'PATCH')}

    if 'command' in user_request:
        action, method = commands.get(user_request['command'], (None, None))

        if action and request.method == method:
            return action(kwargs)