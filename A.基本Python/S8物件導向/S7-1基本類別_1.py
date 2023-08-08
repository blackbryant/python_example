#物件導向-類別與物件

#定義類別
#以動物"狗"為例
class Dog():
    def __init__(self,name) : #定義建構子
        self.name=name
        self.age =1           #初始化年齡為1
    def bite(self):   #定義方法 "咬"
        print("咬")
    def eat(self):    #定義方法 "吃"
        print("吃")

#建立實例
dog = Dog("貴賓狗")
#呼叫方法
print("動物:"+dog.name)
dog.bite()
dog.eat()


 
#封裝:私有函式/屬性
#
#私有屬性:表示外部無法讀取或是修改該屬性的值。 宣告方式:__名稱
#公有屬性:表示外部可以直接讀取或是修改該屬性的值。
#
#私有方法:表示外部無法讀取方法。 宣告方式:__方法名稱
#公有方法:表示外部直接讀取方法。 

##範例:
class PrivateDog():
    def __init__(self,name) : # 建構子
        self.__name=name      # 私有屬性
        self.age=1
        self.__sex="M"        # 私有屬性
    def bite(self):           # 公有方法
        print("咬")
    def eat(self):
        print("吃")
    def info(self):
        self.__age()
    def __age(self):          #私有方法
        print("大概"+str(self.age)+"歲")

dog = PrivateDog("貴賓狗")
#出現錯誤，因為name為私有屬性，無法提供外部使用
#print("動物名稱:"+dog.name)   #AttributeError: 'PrivateDog' object has no attribute 'name'
dog.bite()
dog.eat()
dog.info()
#dog.__age()  #發生'Dog2' object has no attribute '__age' 錯誤，因為為私有函式

#高手破解: 使用實例.__類別名稱__屬性  ，還可以讀取私有屬性
print("動物名稱:"+dog._PrivateDog__name)

#高手破解: 使用實例.__類別名稱__方法  ，還可以讀取私有屬性
print("動物私有方法:")
dog._PrivateDog__age()
###################################################################################
print("############################繼承##########################")
#類別繼承
#父類別、基底類別、超類別(superclass)
#父類別:動物
class Animal():
    def __init__(self) -> None:
        self.__age =1
        pass
    def bite(self):           # 公有方法
        print("咬")
    def eat(self): 
        print("吃")
    def fly(self):
        print("飛")
    def age(self):
        return self.__age     #利用return回傳私有的值

#子類別:狗
class Dog(Animal):
    def fly(self):
        print("不會飛")
_animal = Animal()
_dog = Dog()
print("呼叫父類別")
_animal.bite()
_animal.eat()
_animal.fly()
print("呼叫子類別")
_dog.bite()
_dog.eat()   #
_dog.fly()   #如果子類別有定義fly()，就要呼叫子類別的函式




#######################################################################

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




