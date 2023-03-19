from flask import request
from controller.login import logout_user
from controller.project import create_project, archive_project
from model.dashboard.crud import open_dashboard

def dashboard_system():
    user_request = request.get_json()

    commands = {'open_dashboard': (open_dashboard, 'GET'),
                'create_project': (create_project, 'POST'),
                'archive_project': (archive_project, 'PATCH'),
                'logout_user': (logout_user, 'PATCH')}
    
    if 'command' in user_request:
        action, method = commands.get(user_request['command'], (None, None))

        if action and request.method == method:
            return action()
        