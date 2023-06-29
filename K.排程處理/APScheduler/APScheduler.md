##### Apscheduler教學

* 它具有強大任務調度、完成定時、週期任務，他可以跨平台的執行，用來取代linux平台上的cron daemon或是window task scheduler
  
* 任務
> 1. Cron形式
> 2. 間隔執行
> 3. 僅有執行一次

* 資料儲存
> Momery , SQL DB, MongoDB, Redis, ZooKeeper

* 安裝: pip install Apscheduler教學

##### 基本概念
    Scheduler -> trigger 
              -> job stores
              -> executors  

解釋其中兩種調度器BackgroundScheduler和BlockingScheduler的區別
BackgroundScheduler: 调用start后主线程不会阻塞。当你不运行任何其他框架时使用&#xff0c;并希望调度器在你应用的后台执行
BlockingScheduler:会阻塞主线程的运行，调用start函数后会阻塞当前线程。当调度器是你应用中唯一要运行的东西时
> BlockingScheduler
> scheduler.shutdown(wait=False) 加上這個不會發生阻塞，但是只會執行一次

* 想要在start調度後，執行job()立即執行
> my_func()
> job_id1= scheduler.add_job(my_func,'interval', seconds=3)
> while(True):
>      #主要的執行續不會執行到
>      print("main===")
>      time.sleep(2)

