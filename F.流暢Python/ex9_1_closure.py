#第九章 函数装饰器和闭包

#閉包寫法，該方法效率不高，因為series需要記憶所有的值
def make_average():
    series=[]
    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return average

#avg = make_average()
#avg(10)
#avg(11)
#avg(12)

#UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
def make_average2():
    count=0
    total=0
    def average(new_value):
        nonlocal count, total #將變數宣告成自由變數
        count +=1
        total += new_value
        
        return total / count
    return average


avg2 = make_average2()
avg2(10)
print(avg2(11))
print(avg2(12))

#裝飾器 缺點不支援參數
import time
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elaped = time.perf_counter() - t0
        name=func.__name__
        arg_str= ','.join(repr(arg) for arg in args)
        print(f'[{elaped:0.8f}s] {name}({arg_str})->{result!r}')
        return result
    return clocked

@clock
def factorial(n):
    return 1 if n<2 else n * factorial(n-1)

@clock
def snooze(seconds):
    time.sleep(seconds)

snooze(10)
print("6! =",factorial(6))




import time
def clock(func):
    def clocked(*args,**kwargs):
        t0 = time.perf_counter()
        result = func(*args,**kwargs)
        elaped = time.perf_counter() - t0
        name=func.__name__
        arg_str= ','.join(repr(arg) for arg in args)
        print(f'[{elaped:0.8f}s] {name}({arg_str})->{result!r}')
        return result
    return clocked







