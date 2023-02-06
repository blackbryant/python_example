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

