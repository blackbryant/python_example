# -*- coding: utf-8 -*-


# 注册蓝本 必须用下列顺序 避免陷入循环依赖
from flask import Blueprint
job = Blueprint('job', __name__)

from . import views, core