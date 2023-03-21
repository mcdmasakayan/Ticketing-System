from flask import redirect, url_for
from model.project.crud import generate_project, show_project, cache_project, edit_project

def create_project():
    response = generate_project()

    return response

def open_project(**kwargs):
    response = redirect(url_for('bp.show_project', kwargs))

    return response

def archive_project(**kwargs):
    response = cache_project(kwargs)

    return response

def modify_project(**kwargs):
    response = edit_project(kwargs)

    return response