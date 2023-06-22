#字典
#建立方式一、 {鍵1:值1,鍵2:值2}
dict1 = {"A":41,"B":42}
#建立方式二、dict = dict([[鍵1,值1],[鍵2,值2]])
dict2 = dict([["A",41],["B",42]])
#建立方式三、dict = dict(鍵1=值1,鍵2=值2)
dict3 = dict(A=41,B=42)

print("A:"+str(dict3['A']))
#print("A:"+str(dict3[0])) //錯誤
print("A"+str(dict3))

#為了沒有取到值而發生錯誤，使用dict.get()

#修改字典
dict2 = dict([["A",41],["B",42]])
dict2['A'] = 60
print(dict2['A'])

#刪除字典
del dict2['A']
print(dict2)

#刪除所有元素
dict2.clear()
print(dict2)

#刪除字典
del dict2

#============================f進階字典====================
dict3 = {"apple":50,"banana":60,"grape":100}
#1. len(dict1)
print(len(dict3))

#2. dict3.copy()
dict4 = dict3.copy()
print(dict4)

#3. 檢查健值是否存在
isExist = 'banana' in dict4
print(isExist)

#4. dict3.items() 以健-值組為元素的組合
print(dict3.items())

#5. dict3.keys() 以鍵為元素的組合
print(dict3.keys())

#6. dict3.values() 以值為元素的組合

#7. in名稱
print("apple" in dict3)
print("apple2" in dict3)

#8. dict3.setdefault(key,value)
#(1) 沒有傳入預設值: 鍵值存在，回傳值
#(2) 沒有傳入預設值: 鍵值不存在，回傳None
#(3) 有傳入預設值: 鍵值存在，回傳值
#(4) 有傳入預設值: 鍵值不存在，回傳預設值
dict3.setdefault("strawbetty")



