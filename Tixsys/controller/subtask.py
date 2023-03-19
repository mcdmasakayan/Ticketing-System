from model.subtask.crud import create_subtask, archive_subtask, toggle_subtask

def new_subtask(kwargs):
    response = create_subtask(kwargs)

    return response

def remove_subtask(kwargs):
    response = archive_subtask(kwargs)

    return response

def complete_subtask(kwargs):
    response = toggle_subtask(kwargs)

    return response