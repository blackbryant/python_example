import array
from collections import namedtuple
#序列的陣列

x='ABC'
dummy = [ord(x) for x in x]

print(dummy)
print(x)
print("============笛卡兒 乘積=============")
colors=['black','white']
sizes=['S','M','L']
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)

print("==============產生器表達式=用圓括弧===============")
symbols = '$¢£¥€¤'
a= tuple(ord(symbol) for symbol in symbols)
print(a)

aa=array.array('I',(ord(symbol) for symbol in symbols ))
print(aa)
#產生器
for tshirt in ('%s %s' % (color, size) for color in colors for size in sizes):
    print(tshirt) 

print("===========*抓取任意數量的引數===========")
a,b, *rest = range(5)
print(a,b,rest)
a,b, *rest = range(2)
print(a,b,rest)

print("=====================collections=====================")
City = namedtuple("City",'name country population coordinates')
tokyo = City('Tokey','JP', 36.933, (35.689722,139.691667))
print(tokyo)
print(tokyo._fields) # list all fields 


############################
#range() and slice 要排除最後一個項目
#slice物件 [from:to:step]
s='bicycle'
print(s[::2])
print(s[1:3])
print(s[::-1]) # reserver

# * 
l=[1,2,3]
print(l *5)




