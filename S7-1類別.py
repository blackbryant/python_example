#物件導向-類別與物件
#
class Dog():
    def __init__(self,name) : #建構子
        self.name=name
    def bite(self):   #方法
        print("咬")
    def eat(self):
        print("吃")

dog = Dog("貴賓狗")
print("動物:"+dog.name)
dog.bite()
dog.eat()

#封裝:私有函式
class Dog2():
    def __init__(self,name,age) : #建構子
        self.name=name
        self.age=age
    def bite(self):   #方法
        print("咬")
    def eat(self):
        print("吃")
    def info(self):
        self.__age()
    def __age(self):
        print("大概"+str(self.age)+"歲")

dog = Dog2("貴賓狗",10)
print("動物:"+dog.name)
dog.bite()
dog.eat()
dog.info()
#dog.__age()  #發生'Dog2' object has no attribute '__age' 錯誤，因為為私有函式

#多型
print("====================多型========================")
class Bird():
    def __init__(self,name):
        self.name = name
        print("父類別:"+name)
    def fly(self):
        print("鳥在飛")
class Plane(Bird):
    def __init__(self,name):
        super().__init__(name)
    def fly(self,category):
        print(category,"在飛",end=",")

b1 = Bird("鳥")
b1.fly()

p1 = Plane("測試版")
p1.fly("戰鬥機")












#




