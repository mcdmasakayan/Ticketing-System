from datetime import datetime, timedelta
from model.init_db import db
from model.user.data import User
from model.project.data import Project
from model.task.data import Task
from model.subtask.data import Subtask

def delete_archived(**args):
        expiration = datetime.now() - timedelta(seconds=5)
        Project.query.filter(Project.date_created <= expiration).filter_by(archived=True).delete()
     
        db.session.commit()