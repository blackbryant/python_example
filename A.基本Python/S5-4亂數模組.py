#
#import 模組名稱
#import random

# from 模組名稱 import *
from random import *
print(randint(10,20))

# import 模組名稱 as r
import random as r
r.randint(10,20)

#choice(字串或是串列)，隨機取出1個元素
print(r.choice("abcdefghijklm"))

#random() : 0~1隨機的浮點數
print(r.random())

#randrange(n1,n2,step):n1~n2之間每隔step取出
print(r.randrange(1,10,2))

# sample(字串,n)，隨機取出n個元素
stra ="abcdefghijklm"
a = r.sample(stra,3)
print(a)

#shuffle(list) 串列洗牌
print(r.shuffle(['a','b','c','d']))

#uniform(f1,f2):從f1到f2凗機取一個浮點數
print(r.uniform(10,100))
