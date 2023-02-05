# 3.2 進階串列與元組
#
list1= [1,2,3,4]
#重複n次
list2 = list1*2
print(list2);
#取出區間n~m
print(list1[1:3])
#刪除元素,索引值m
del list1[1]
print(list1)
#min(list), max(list)
print(min(list1))
print(max(list1))
#list.index(元素值)
print(list1.index(3))
#重複出現次數：list.count(元素值)
print(list2.count(2))
#加在該串列最後一位：list.append(元素) ，元素可以是陣列或是單值
list1.append(1)
#list.extend(newList) , 元素只能是串列
xlist=[10]
list2.extend(xlist)
print(list2)
#插入元素:list.insert()

#element = list.pop()或list.pop(索引值)
#將元素取出並移除
list1.pop()
#list.remove(元素值)
list1.remove(3)
print(list1)
#反轉串列順序:list.reverse()
list2.reverse()
print(list2)

#串列小到大排序
list1.sort()

#以串列計算薪資所得
employ_salary=[30000,38000,42000,48000,52000]
sum =0;
for salary in employ_salary:
    sum += salary
print(sum)

##########元組(Tuple)###########
#由 value,
typle1 = (1,2,3,4,5)
typle2 = (1,"香蕉",2)
print(typle1[1])
print(len(typle1))

#元組與串列的比較
#1. 執行速度比串列
#2. 存於元組的資料為安全:因為內容無法改變

#元組與串列轉換
tupleA=[1,2,3,4]
listA=list(tupleA)
listA.append(8)
print(listA)

listB=[1,2,3,5]
tupleB = tuple(listB)
#tupleB.append(8) #發生錯誤
print(tupleB)
