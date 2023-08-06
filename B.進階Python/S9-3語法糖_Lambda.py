#Lambda函式，也稱匿名函式，不需要定義函式名稱，只能一行運算式，語法簡潔有力
#
#基本語法: lambda parameter_list: expression
#Lambda函式的傳入參數，可以有多個
multipy = lambda x ,y : x*y
print(multipy(2,2))

#Lambda函式支援IIFE(immediately invoked function expression)語法
print((lambda x,y : x+y)(9,8))

###################lambda function #################
#filter()：在可疊代的物件中，依據條件運算式
#filter(lambda parameter: expression, iterable)

numbers=[1,2,3,4,5,10,20,30,40,50]
result = filter(lambda x : x<10, numbers) # result iterator
print(list(result))

# map()：在可疊代的物件中，套用特定運算式於每一個元素
# map()內建方法會將串列(List)中的每個元素傳入Lambda函式進行特定的運算，最後回傳每個元素的運算結果
numbers=[1,2,3,4,5,10,20,30,40,50]
result = map(lambda x : x *2 ,numbers)
print(list(result))

#reduce()：與map()內建方法同樣在可疊代的物件中，
#將可疊代物件中的前兩個元素先進行Lambda運算式的運算。
#接著將第一個步驟的運算結果和可疊代物件中的下一個元素(第三個)傳入Lambda函式進行運算。
#依此類推，直到可疊代物件的元素都運算完成。
#reduce(lambda parameter1, parameter2: expression, iterable)

from functools import reduce
numbers=[1,2,3,4,5,10,20,30,40,50]
result = reduce(lambda x,y : x+y ,numbers)
print(result)

#sorted()：用來排序可疊代物件中的元素
#sorted(iterable, key=lambda parameter: expression)
cars = [("mazda",30),("toyoza",10),("benz",15),("bmw",50)]
print(sorted(cars, key=lambda car :car[0]))


#Lambda函式 vs 一般函式(Function)
#1.Lambda函式不需要函式名稱，
#2.Lambda函式只能有一行運算式
#3.Lambda在每一次運算完會自動回傳結果，一般函式回傳需要return

#使用時機:
# Lambda函式故然只需要一行就可以解決運算問題，但是也建議不要過度使用或是複雜寫法，讓程式維護不好解讀，
# 如果遇到複雜的邏輯，還是優先選擇一般函式完成

