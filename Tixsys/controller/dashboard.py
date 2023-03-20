from controller.project import create_project, archive_project
from model.dashboard.crud import open_dashboard

def show_dashboard_data():
    response = open_dashboard()

    return response

def generate_project():
    response = create_project()

    return response

def remove_project():
    response = archive_project()

    return response