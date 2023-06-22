import random as r
#骰子遊戲
while True:
    input_data = input("按下任意鍵，甩骰子，或直接按[enter]:")
    if len(input_data)>0:
        num = r.randint(1,6) 
        print("得到數字為:"+str(num))
    else:
        print("結束")
        break