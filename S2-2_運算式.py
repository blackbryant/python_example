#運算式
#1.單元運算子: -100, not x 

#2.二元運算子: 
# 四則運算: + - * / % // **
# 比較運算: == != > < >= <=
# 邏輯運算: not and or
# 複合指定運算: += -= *= /= %= //= **=
nat = input("輸入國文成績:")
math = input("輸入數學成績:")
eng = input("輸入英文成績:")
sum = int(nat) + int(math) + int(eng)
average = sum /3
print("總成績%d, 成績：%3.2f"%(sum,average))
