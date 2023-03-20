from flask import Blueprint
from controller.login import login_system
from controller.project import project_system
from controller.task import task_system
from controller.dashboard import dashboard_system
from controller.settings import settings_system
from middleware.process import delete_archived

bp = Blueprint('bp', __name__)
bp.before_request(delete_archived)
bp.route('/dashboard/settings', methods=['GET', 'PATCH'])(settings_system)
bp.route('/login', methods=['POST'])(login_system)
bp.route('/dashboard', methods=['GET', 'POST', 'PATCH'])(dashboard_system)
bp.route('/dashboard/<string:project_name>', methods=['GET', 'POST', 'PATCH'])(project_system)
bp.route('/dashboard/<string:project_name>/<string:task_name>', methods=['GET', 'POST', 'PATCH'])(task_system)