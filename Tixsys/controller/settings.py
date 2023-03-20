from flask import request
from model.settings.crud import archive_user, quit_user

def remove_user(**kwargs):
    response = archive_user(kwargs)

    return response

def logout_user():
    response = quit_user()

    return response