''''
APS排程
'''
import time 
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO,filename="log.log",filemode="a")
scheduler = BlockingScheduler(timezone="Asia/Taipei")

def my_func():
     logging.info(f"my_func =====")
     print(f'工作１啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

job = scheduler.add_job(func=my_func,trigger="interval",seconds=10)

scheduler.start()
logging.info(f"scheduler start !")