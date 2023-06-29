from apscheduler.schedulers.background import BackgroundScheduler
import time
def my_func():
    print("A task begins")
    print("It sum number from  1 to 10 ")
    

scheduler = BackgroundScheduler() 
job_id = scheduler.add_job(my_func,'interval', seconds=3)
scheduler.start()

try:
    
    while True:
        print("===main===")
        time.sleep(2)
except:
        scheduler.shutdown() 


