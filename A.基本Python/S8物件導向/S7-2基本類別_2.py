#type and instance
class Elementary:
    pass
class Senior:
    pass


class College:
    '''說明:大學類別
    '''
    def __init__(self):
        self.__name="大學"
    def tuition(self):
        self.tuition = 1000 
    

elem = Elementary()
senior = Senior()
college = College()

print("Elementary 物件類別:",type(elem)) #Elementary 物件類別: <class '__main__.Elementary'>
print("Senior 物件類別:",type(senior))   #Senior 物件類別: <class '__main__.Senior'>
print("College 物件類別:",type(college)) #College 物件類別: <class '__main__.College'>

#isinstance(實例，類別) :是否該實例是屬於類別
#
print("elem 實例是否屬於 Elementary 物件類別:",isinstance(elem,Elementary))  #True
print("elem 實例是否屬於 Senior 物件類別:",isinstance(elem,Senior))          #False
print("elem 實例是否屬於 College 物件類別:",isinstance(elem,College))        #False
print("senior 實例是否屬於 Elementary 物件類別:",isinstance(senior,Elementary))  #False
print("senior 實例是否屬於 Senior 物件類別:",isinstance(senior,Senior))          #True
print("senior 實例是否屬於 College 物件類別:",isinstance(senior,College))        #False
print("college 實例是否屬於 Elementary 物件類別:",isinstance(college,Elementary))  #False
print("college 實例是否屬於 Senior 物件類別:",isinstance(college,Senior))          #False
print("college 實例是否屬於 College 物件類別:",isinstance(college,College))        #True

#其他
#dir():環境變數、方法
print(dir())
#(1)__doc__ 文件
print(college.__doc__)

#(2) 
if __name__=="__main__":  #程式是自己執行，會跑這一段
    print("")

#(3) __str__()

class College2:
    def __init__(self):
        self.name="大學"
        self.tuition = 100
    def __str__(self):
        return f"name:{self.name}  tuition:{self.tuition}"

college2 = College2()
print(college2)













