
#運用 Comprehensions 寫出更高效程式，可以將多行的迴圈濃縮成一行表示(one line expression )
#Comprehensions 解析，
# 語法 [outout for i in list  if condition]
# 範例 [ i**3 for i in [1,2,3,4] if i>2]

#一般for迴圈寫法
nums = [1,2,3,4,5,6,7,8,9]
for num in nums:
    print(num)
#Comprehensions 寫法
print([num for num in nums])


#一般for迴圈寫法+條件判斷
nums = [1,2,3,4,5,6,7,8,9]
for num in nums:
    if num > 5:
        print(num)

#Comprehensions+if 寫法
print([num for num in nums if num >5])

#儲存另一個變數
nums = [1,2,3,4,5,6,7,8,9]
double_nums =[]
for num in nums:
    double_nums.append(num*2)

#Comprehensions 寫法
print([num*2 for num in nums])

##############################################
#List Comprehensions
[i for i in range(4) ]
[2*i for  i in range(4)]

#tuple Comprehensions
#會將tuple結果轉成list
[i for i in (0,2,4,6)]

#set Comprehensions
{i for i in range(4)}

#Generator Comprehensions
#<generator object <genexpr> at 0x00000274BB614930>
gen= (i for i in range(4))
print(gen)

###進階
#Nested Comprehensions
#注意: 最好不要超過兩層以上，不然會影響可讀性
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]
nested_ex = [(i,j) for i in range(4) for j in range(3)]
print(nested_ex)


#lambda VS Comprehensions VS 傳統迴圈
#list(map(lambda x : x**2 ,nums)) VS  [i**2 for i in range(4) ] VS 傳統迴圈
#效能上比較: numpy > map ~= Comprehensions > 傳統迴圈
# Plat >> Nested 原則


