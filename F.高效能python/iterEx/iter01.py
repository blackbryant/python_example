 
iter1 = [1,2,3,4,5].__iter__()
print(iter1.__length_hint__())
print(iter1.__next__())
print(iter1.__next__())

#迭代器取直
while True:
    try:
        item = iter1.__next__()
        print(item)
    except StopIteration:
       break
print("==========生成器===========")
#生成器
def produce():
    for i in range(200000):
        yield "%s"%i

p= produce()
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())




