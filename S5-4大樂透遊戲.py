import random as r
#大樂透遊戲
list1 = r.sample(range(1,50),7)
special_num = list1.pop()
list1.sort()
print("本期大樂透號碼:",end="")
for i in range(0,6):
    if i==5 :
        print(str(list1[i]))
    else:
        print(str(list1[i]),end=",")
print("本期大特透特別號:"+str(special_num))
