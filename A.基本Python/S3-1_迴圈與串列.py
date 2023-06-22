# 3.1 迴圈與串列
# 1. 串列
# 串列名稱 = [元素1, 元素2, ...]
# 索引值:0 
list1= [1,2,3,4,5]
list2 = ["香蕉","蘋果","橘子"]
print(list2[1]) # 蘋果
print(list2[-1]) # 橘子

#3.2 range 函式
#
r1 = range(5) # [0,1,2,3,4]
#
r2 = range(3,8) #[3,4,5,6,7]
#
r3 = range(3,8,2) #[3,5,6,7]
r4 = range(8,3,-1) #[8,7,6,5,4]
#
#3.1 迴圈
#
#
for i in range(1,11):
    print(i)
# break , continue

#While
n=0
total=0
while(n<10):
    n+=1
    total+=n
print(total)

