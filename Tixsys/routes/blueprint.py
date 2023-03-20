from flask import Blueprint
from controller.login import login_system
from controller.project import project_system
from controller.task import task_system
from controller.dashboard import dashboard_system
from controller.settings import settings_system

bp = Blueprint('bp', __name__)
#bp.route('/dashboard/settings', methods=['GET', 'PATCH'])(settings_system)
bp.route('dashboard/settings/archived_user', methods=['PATCH'])(archived_user)
bp.route('dashboard/settings/logout', methods=['PATCH'])(logout_user)
#bp.route('/login', methods=['POST'])(login_system)
bp.route('/login/login_user', methods=['POST'])(verify_user)
bp.route('/login/register_user', methods=['POST'])(register_user)
#bp.route('/dashboard', methods=['GET', 'POST', 'PATCH'])(dashboard_system)
bp.route('/dashboard/open_dashboard', methods=['GET'])(open_dashboard)
bp.route('/dashboard/create_project', methods=['POST'])(create_project)
bp.route('/dashboard/archive_project', methods=['PATCH'])(archive_project)
#bp.route('/dashboard/<string:project_name>', methods=['GET', 'POST', 'PATCH'])(project_system)
bp.route('/dashboard/<string:project_name>/create_project', methods=['POST'])(create_project)
bp.route('/dashboard/<string:project_name>/open_project', methods=['GET'])(open_project)
bp.route('/dashboard/<string:project_name>/archive_project', methods=['PATCH'])(archive_project)
bp.route('/dashboard/<string:project_name>/modify_project', methods=['PATCH'])(modify_project)
bp.route('/dashboard/<string:project_name>/create_task', methods=['POST'])(create_task)
bp.route('/dashboard/<string:project_name>/archive_task', methods=['PATCH'])(archive_task)
bp.route('/dashboard/<string:project_name>/move_task', methods=['PATCH'])(move_task)
#bp.route('/dashboard/<string:project_name>/<string:task_name>', methods=['GET', 'POST', 'PATCH'])(task_system)
bp.route('/dashboard/<string:project_name>/<string:task_name>/create_task', methods=['POST'])(create_task)
bp.route('/dashboard/<string:project_name>/<string:task_name>/open_task', methods=['GET'])(open_task)
bp.route('/dashboard/<string:project_name>/<string:task_name>/archive_task', methods=['PATCH'])(archive_task)
bp.route('/dashboard/<string:project_name>/<string:task_name>/transfer_task', methods=['PATCH'])(move_task)
bp.route('/dashboard/<string:project_name>/<string:task_name>/modify_task', methods=['PATCH'])(modify_task)
bp.route('/dashboard/<string:project_name>/<string:task_name>/create_subtask', methods=['POST'])(new_subtask)
bp.route('/dashboard/<string:project_name>/<string:task_name>/archive_task', methods=['PATCH'])(remove_subtask)
bp.route('/dashboard/<string:project_name>/<string:task_name>/create_task', methods=['PATCH'])(complete_subtask)