from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from .extesions import db

class TaskLog(db.Model):
    __tablename__ = 'task_log'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String(16))
    status = db.Column(db.Boolean)
    exe_time = db.Column(db.DateTime, default=datetime.now)
    cmd = db.Column(db.String(128))
    stdout = db.Column(db.Text)

    def to_json(self):
        json_post = {
            'id': self.id,
            'task_id': self.task_id,
            'status': self.status,
            'exe_time': self.exe_time,
            'cmd': self.cmd,
            'stdout': self.stdout
        }
        return json_post
