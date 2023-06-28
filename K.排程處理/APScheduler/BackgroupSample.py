from apscheduler.schedulers.background import BackgroundScheduler

def my_func():
    print("A task begins")
    print("It sum number from  1 to 10 ")
    sum=0
    for i in 11:
        sum +=i
    print(sum)

scheduler = BackgroundScheduler() 
job = scheduler.add_job(my_func,'interval',minutes=2)
