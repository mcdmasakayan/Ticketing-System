from flask import request
from controller.task import create_task, move_task, archive_task
from model.project.crud import create_project, open_project, archive_project

def project_system(**kwargs):
    user_request = request.get_json()
    commands = {'create_project': (create_project, 'POST'),
                'open_project': (open_project, 'GET'),
                'archive_project': (archive_project, 'PATCH'),
                'create_task': (create_task, 'POST'),
                'archive_task': (archive_task, 'PATCH'),
                'move_task': (move_task, 'PATCH')}
    
    if 'command' in user_request:
        action, method = commands.get(user_request['command'], (None, None))

        if action and request.method == method:
            return action(kwargs)