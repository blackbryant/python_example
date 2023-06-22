#Object References, Mutability,and Recycling
#
#
#1.Variables Are Not Boxes : Label
#Variables a and b hold references to the same list, not copies of the list
#說明:the b = a statement does not copy the contents of box a into box b. It
#attaches the label b to the object that already has the label a.

a = [1, 2, 3] 
b=a
a.append(4)
print("a:"+str(a))
print("b:"+str(b))

#2.x = … binds the x name to the object created or referenced on the righthand side.
class Gizmo:
    def __init__(self):
        print(f'Gizmo id: {id(self)}')
x = Gizmo()
print(x)
#y = Gizmo() * 10
#print(y)
#['Gizmo', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'x']
print(dir())

#2. Identity, Equality, and Aliases
#
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print("{0},{1} ".format(id(charles), id(lewis)))
lewis['balance'] = 950
print(lewis)
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950} 
print(alex == charles)  #trure ; The objects bound to alex and charles have the same value
print(id(alex)) #id() returns the memory address of the object
print(alex is not charles) #The is operator compares the identity of two objects; 

#3. Choosing Between == and is
# The == operator compares the values of objects 
# The is operator computing is as simple as comparing two integer IDs
#In contrast, a == b is syntactic sugar for a.__eq__(b). The __eq__ method inherited from object compares object IDs, so it
#produces the same result as is. 
t1 = (1, 2, [30, 40]) 
t2 = (1, 2, [30, 40])
print(t1==t2)
print(id(t1[-1]))
t1[-1].append(99) 
print(t1)
#Copies Are Shallow by Default
l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)  #list(l1) creates a copy of l1.
print("l1:"+str(l1))
print("l2:"+str(l2))
print(l2 == l1) #內容相同，
print(12 is l1 ) # ids are  different

#The Relative Immutability of Tuples
t1 = (1, 2, [30, 40]) 
t2 = (1, 2, [30, 40]) 
print(t1 == t2) #兩個set內的元素是相同

print(id(t1[-1]))
print(t1[-1].append(99))
print(t1)
print(id(t1[-1]))
print(t1==t2)


#Copies Are Shallow by Default

l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)      
print(l1==l2)
print(l1 is l2) #but refer to two different objects.
#shallow copy
#the outermost container is duplicated, but the copy is filled with references to the same items held by the original container
#This saves memory and causes no problems if all the items are immutable
l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22] 
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)

#Deep and Shallow Copies of Arbitrary Objects
import copy
class Bus:
 def __init__(self, passengers=None):
    if passengers is None:
        self.passengers = []
    else:
        self.passengers = list(passengers)
 def pick(self, name):
    self.passengers.append(name)
 def drop(self, name):
    self.passengers.remove(name)


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)     #shallow copy
bus3 = copy.deepcopy(bus1) #deep copy
print(id(bus1), id(bus2), id(bus3))
bus1.drop('Bill')
print(bus2.passengers)
#bus1 and bus2 share the same list object, because bus2 is a shallow copy of bus1.
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)) #
print(bus3.passengers)#bus3 is a deep copy of bus1, so its passengers attribute refers to another list

#copy: __copy__()
#deepcopy: __deepcopy__() 

#4.Function Parameters as References
#===Call by sharing===
#means that each formal parameter of the function gets a copy of each reference in the arguments
def f(a, b): 
   a += b
   return a


#Defensive Programming with Mutable Parameters
#當我們把參數當作輸入條件時，我們需要考慮parameter是否會被影響內容值
#Best Pratice
class TwilightBus:
 """A bus model that makes passengers vanish"""
 def __init__(self, passengers=None):
    if passengers is None:
        self.passengers = [] 
    else:
       self.passengers = list(passengers)  #Make a copy of the passengers list,
 def pick(self, name):
    self.passengers.append(name)
 def drop(self, name):
    self.passengers.remove(name)

#del and Garbage Collection
#1.del deletes references, not objects.
#2. __del__ is invoked by the Python interpreter when the instance is about to be destroyed to give it a chance to release external resources.
# https://docs.python.org/3/reference/datamodel.html#object.%5C_%5C_del__
#在不同CPython , PyPy
#In CPython, the primary algorithm for garbage collection is reference counting.that refcount reaches zero, the object is immediately destroyed:
#
#The weakref module allows the Python programmer to create weak references to objects.
#弱引用通常會使用在 circular reference、caches 或是需要存放大型物件的地方
#參考:https://blog.louie.lu/2017/07/29/%E4%BD%A0%E6%89%80%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-python-%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB%E7%94%A8%E6%B3%95-04-weakref/?fbclid=IwAR0tFsR4l3naU6V1gls1AWMpZvkTIXfEfokEQT-I0CARP-MZd9PGxdbCCWg
import weakref
import sys
s1 = {1, 2, 3}
s2 = s1 
print(sys.getrefcount(s1))
def bye(): 
    print('...like tears in the rain.')
ender = weakref.finalize(s1, bye)  # It is about to be destroyed or otherwise hold a reference to it
print(ender.alive)
# del does not delete objects,the s1 reference was passed to the finalize function, which must have held
# on to it in order to monitor the object and invoke the callback. 
#
del s1
print(ender.alive) # true
s2 = 'spam' 
print(ender.alive) # false

# tuple()和t1[:]t[:] does not make a copy, but returns a reference to the same object.
t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1)
print(id(t1),id(t2))
t3= t1[:]
print(t3 is t1)
t1 = (1, 2, 3)
t3 = (1, 2, 3) 
t3 is t1 
s1 = 'ABC'
s2 = 'ABC' 
s2 is s1









