from flask import request
from controller.subtask import new_subtask, remove_subtask, complete_subtask
from model.task.crud import create_task, open_task, archive_task, move_task, modify_task

def task_system(**kwargs):
    user_request = request.get_json()
    commands = {'create_task':(create_task, 'POST'),
                'open_task':(open_task, 'GET'),
                'archive_task':(archive_task, 'PATCH'),
                'transfer_task':(move_task, 'PATCH'),
                'modify_task':(modify_task, 'PATCH'),
                'create_subtask':(new_subtask, 'POST'),
                'archive_subtask':(remove_subtask, 'PATCH'),
                'complete_subtask':(complete_subtask, 'PATCH')}

def create_task(kwargs):
    response = create_task (kwargs)

    return response

def open_task(kwargs):
    response = open_task(kwargs)

    return response

def archive_task(kwargs):
    response = archive_task(kwargs)

    return response

def transfer_task(kwargs):
    response = move_task(kwargs)

    return response

def modify_task(kwargs):
    response = modify_task(kwargs)