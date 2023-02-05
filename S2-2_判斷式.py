#判斷式
#1.判斷式
#if...elif...else
#
score =100
if(score>60):
    comment="及格"
if(score>60):
    comment="及格"
else:
    comment="不及格"

if(score<60):
    comment="不及格"
elif(score>80 and score<90 ):
    comment="良好"
elif(score>90 and score<=100 ):
    comment="優等"
print(comment)

#百貨公司折扣戰
#100000元打8折;50000打8.5折;30000打9折;10000打9.5折
money = int(input("輸入購物金額:"))
if(money >=10000):
    if(money>=1000000):
        print(money * 8,end="元\n")
    elif(money>=50000):
         print(money * 8.5,end="元\n")
    elif(money>=30000):
         print(money * 9,end="元\n")
    else:
        print(money * 9.5,end="元\n")
else:
    print(money ,end="元\n")

#2.迴圈




