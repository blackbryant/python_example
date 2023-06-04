from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from flask_moment import Moment
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
db = SQLAlchemy()
# task sevices
scheduler = APScheduler()
moment = Moment()
