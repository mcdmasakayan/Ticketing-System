from controller.subtask import create_subtask, archive_subtask, complete_subtask
from model.task.crud import create_task, open_task, archive_task, move_task, modify_task

def create_task(kwargs):
    response = create_task (kwargs)

    return response

def open_task(kwargs):
    response = open_task(kwargs)

    return response

def archive_task(kwargs):
    response = archive_task(kwargs)

    return response

def move_task(kwargs):
    response = move_task(kwargs)

    return response

def modify_task(kwargs):
    response = modify_task(kwargs)

def create_subtask(kwargs):
    response = create_subtask(kwargs)

    return response

def archive_subtask(kwargs):
    response = archive_subtask(kwargs)

    return response

def complete_subtask(kwargs):
    response = complete_subtask(kwargs)

    return response