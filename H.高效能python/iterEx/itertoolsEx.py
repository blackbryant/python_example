from itertools import accumulate
import itertools


#累加
a=[2,4,6,8,10]
itor01 = accumulate(a)
for v in itor01:
    print(v)

#chain
print("=====chain=======")
a=[2,4,6,8]
b=[1,2,3,4,5]
iter_ab = itertools.chain(a,b) #可以多個
for v in iter_ab:
    print(v)

#compress
print("=====compress=======")
items=[1,2,3,4,5,6,7,8,9,10]
selected=[0,1,0,1,0,1,0,1,0,1]
compress_itor = itertools.compress(items,selected)
for v in compress_itor:
    print(v)

#dropwhile:只會true都會丟棄，但是只要遇到true就會停下
print("=====dropwhile=======")
kk=[2,3,4,5,6,7,8,9,10]
def dropItem(e):
    print("e:"+e)
    if (e%2)==0:
        return True
    else:
        return False

dropWhile_iter = itertools.dropwhile(lambda x:x<10,kk)
for v in dropWhile_iter:
    print(v,end=",")
print("")



#
#
#




