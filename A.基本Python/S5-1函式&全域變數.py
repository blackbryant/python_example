#自訂函式
# 無參數與回傳值
def Hello():
    print("Hello World")
Hello()

# 有參數與回傳值
def CalcuateArea(width,height):
    area = width * height
    return area
CalcuateArea(100,10)

#多個回傳值
def Circle(radius):
    area = radius * radius * 3.14 
    length = 2 * radius * 3.14
    return area, length
ans_area, ans_length = Circle(10)
print("circle area:%5.2f , length: %5.2f" %(ans_area,ans_length))
#
# 參數預設值
def GetArea(width, height=5):
    return width * height 

print("===========區域變數=================")
#區域變數
def scope():
    var1 =1 
    print(var1,var2)
var1=10 
var2=20
scope()
print("============全域變數=================")
#全域變數
def scopeg():
    global vara
    vara=1
    varb=2
    print(vara,varb)
vara=10
varb=20
scopeg()
print(vara,varb)


