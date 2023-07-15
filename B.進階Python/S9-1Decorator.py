#Decorator 不改變函式內容的情況下，去增加函式額外功能，可以減少重複程式碼
#

import time
#範例一、紀錄執行程式碼的時間

def execute():
    start = time.time()
    print("execute job!")
    time.sleep(5)
    end = time.time()
    print("execute tiem :", end-start)
    return 

#將計算時間的抽出來為一個函式，再由這個函式呼叫執行程式execute2 
def execute2():
    print("execute job!")
    time.sleep(5)
    return

def cal_time(func):
    start = time.time()
    func()
    end = time.time()
    print("execute tiem :", end-start)
    return
cal_time(execute2)

#Decorator方法
def cal_time_decorator(func):
    def wrap():
        start = time.time()
        func()
        end = time.time()
        print("execute tiem :", end-start)
    return wrap
#不會執行函式
execute2 = cal_time_decorator(execute2)
#實際用才執行，執行名稱都要execute2
execute2()

#語法糖

@cal_time_decorator
def execute3():
    print("execute job!")
    time.sleep(5)
    return
