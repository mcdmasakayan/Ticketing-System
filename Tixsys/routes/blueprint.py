from flask import Blueprint
from controller.login import login_user, register_user
from controller.project import create_project, open_project, archive_project, modify_project, create_task, archive_task, move_task
from controller.task import create_task, open_task, archive_task, move_task, modify_task, create_subtask, archive_subtask, complete_subtask
from controller.dashboard import show_dashboard_data, generate_project, remove_project
from controller.settings import remove_user, logout_user

bp = Blueprint('bp', __name__)

#settings
bp.route('dashboard/settings/archive_user', methods=['PATCH'])(remove_user)
bp.route('dashboard/settings/logout', methods=['PATCH'])(logout_user)

#login system
bp.route('/login/login_user', methods=['POST'])(login_user)
bp.route('/login/register_user', methods=['POST'])(register_user)

#dashboard
bp.route('/dashboard/open_dashboard', methods=['GET'])(show_dashboard_data)
bp.route('/dashboard/create_project', methods=['POST'])(generate_project)
bp.route('/dashboard/archive_project', methods=['PATCH'])(remove_project)

#project
bp.route('/dashboard/<string:project_name>/create_project', methods=['POST'])(create_project)
bp.route('/dashboard/<string:project_name>/open_project', methods=['GET'])(open_project)
bp.route('/dashboard/<string:project_name>/archive_project', methods=['PATCH'])(archive_project)
bp.route('/dashboard/<string:project_name>/modify_project', methods=['PATCH'])(modify_project)
bp.route('/dashboard/<string:project_name>/create_task', methods=['POST'])(create_task)
bp.route('/dashboard/<string:project_name>/archive_task', methods=['PATCH'])(archive_task)
bp.route('/dashboard/<string:project_name>/move_task', methods=['PATCH'])(move_task)

#task
bp.route('/dashboard/<string:project_name>/<string:task_name>/create_task', methods=['POST'])(create_task)
bp.route('/dashboard/<string:project_name>/<string:task_name>/open_task', methods=['GET'])(open_task)
bp.route('/dashboard/<string:project_name>/<string:task_name>/archive_task', methods=['PATCH'])(archive_task)
bp.route('/dashboard/<string:project_name>/<string:task_name>/transfer_task', methods=['PATCH'])(move_task)
bp.route('/dashboard/<string:project_name>/<string:task_name>/modify_task', methods=['PATCH'])(modify_task)
bp.route('/dashboard/<string:project_name>/<string:task_name>/create_subtask', methods=['POST'])(create_subtask)
bp.route('/dashboard/<string:project_name>/<string:task_name>/archive_task', methods=['PATCH'])(archive_subtask)
bp.route('/dashboard/<string:project_name>/<string:task_name>/create_task', methods=['PATCH'])(complete_subtask)