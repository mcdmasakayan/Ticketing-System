from flask import redirect, url_for
from model.project.crud import generate_project, cache_project, edit_project, show_project

def create_project(**kwargs):
    response = generate_project(kwargs)

    return response

def open_project(**kwargs):
    response = redirect(url_for('/dashboard/<string:project_name>', kwargs))

    return response

def archive_project(**kwargs):
    response = cache_project(kwargs)

    return response

def modify_project(**kwargs):
    response = edit_project(kwargs)

    return response