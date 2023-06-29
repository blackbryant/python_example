from apscheduler.schedulers.background import BlockingScheduler
import time



def my_func():
    print("A task begins")
    print("It sum number from  1 to 10 ")
    #scheduler.shutdown(wait=False)


def my_func2(a, b ):
    print("A task begins")
    print(f"It sum number from {a} to {b} ")
    #scheduler.shutdown(wait=False)

def my_alarm():
    print("====my_alarm begins") 
    #scheduler.shutdown(wait=False)

if __name__=="__main__":
    scheduler = BlockingScheduler() 
    job_id1= scheduler.add_job(my_func,'interval', seconds=3)
    job_id2= scheduler.add_job(my_func2,'interval', seconds=5,args=[10,100])
    #指定日期
    job_id3 = scheduler.add_job(my_alarm,"cron",hour=20,minute="*/2")

    scheduler.start()

    
    while(True):
        #主要的執行續不會執行到
        print("main===")
        time.sleep(2)
   


