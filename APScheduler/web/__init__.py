# -*- coding: utf-8 -*-

from flask import Flask
import os,click
from .job import job as job_blueprint
from .main import main as main_blueprint
from .extesions import db,bootstrap,moment,scheduler

def create_app(config_name=None):
    print("CCCCCCCCCCCCCCC")
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')
  
    app = Flask(__name__)    
     
    app.config['SECRET_KEY'] = 'xxxxxxxxx'
    #初始化
    register_extensions(app)
    #註冊網址
    register_blueprints(app)



    app.debug = True
    
    return app


# 注册蓝图
def register_blueprints(app):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(job_blueprint,url_prefix='/v1/cron/job')

def register_extensions(app):
    bootstrap.init_app(app)
    moment.init_app(app)
    scheduler.init_app(app)


# 注册命令
def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    def init():
        """Initialize Albumy."""
        click.echo('Initializing the database...')
        db.create_all()

        #click.echo('Initializing the roles and permissions...')
        
        click.echo('Done.')
