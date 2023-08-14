#正規表達式範例

import re

#(1) 電子郵件檢查
#1.1 中間一定會有 @
#1.2 @ 前面一定是英文 (大小寫皆可)
#1.3 @ 後面一定是「英文 or 數字」 + 「.」 的組合
#1.4 結尾一定是英文
# 正確:
input_mail_01 = "bryant2134aa@gmail.com"
input_mail_02 = "bryant-111-222@gmail.com"
input_mail_03 = "bryant.kim@gmail.com"
error_mail_01 = "bryant2134aagmail.com"
error_mail_02 = "bryant-1234m44@gmail"
error_mail_03 = "bryant-1234m44@gmail"
error_mail_04 = "bryant-1234m44@gmail"
email_rule_template = "^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z]+$"
print(re.fullmatch(email_rule_template,input_mail_01))  #驗證成功，顯示電子郵件
print(re.fullmatch(email_rule_template,input_mail_02))  #驗證成功，顯示電子郵件
print(re.fullmatch(email_rule_template,error_mail_01))  #驗證失敗
print(re.fullmatch(email_rule_template,error_mail_02))  #驗證失敗
print(re.fullmatch(email_rule_template,error_mail_03))  #驗證失敗
print(re.fullmatch(email_rule_template,error_mail_04))  #驗證失敗


 #(2)數字驗證
print("==================數字驗證-1~10======================")
number_rule_template = "^\d{1,10}$"
input_01=  "1234"
input_02=  "1234d"
input_03=  "1234.00"
print(re.fullmatch(number_rule_template,input_01))  #驗證成功
print(re.fullmatch(number_rule_template,input_02))  #驗證失敗
print(re.fullmatch(number_rule_template,input_03))  #驗證失敗

#(3)數字驗證
print("==================數字驗證-小數點======================")
number_rule_template = "^[0-9]+(.[0-9]{1,5})?$"
input_01=  "1234"
input_02=  "1234d.00"
input_03=  "1234.00"
print(re.fullmatch(number_rule_template,input_01))  #驗證成功
print(re.fullmatch(number_rule_template,input_02))  #驗證失敗
print(re.fullmatch(number_rule_template,input_03))  #驗證成功

#(4)手機電話號碼
print("==================手機電話號碼-======================")
#//規則:09開頭，後面接著8個0~9的數字
mobile_rule_template = "^09[0-9]{8}$"
input_01=  "0933123456"
input_02=  "02123456"
input_03=  "12343243"
print(re.fullmatch(mobile_rule_template,input_01))  #驗證成功
print(re.fullmatch(mobile_rule_template,input_02))  #驗證失敗
print(re.fullmatch(mobile_rule_template,input_03))  #驗證失敗


#(4)身分證字號
print("==================身分證字號-======================")
#組合規則:　　　
# (1)英文代號以下表轉換成數字
# A = 10 台北市 J = 18 新竹縣 S = 26 高雄縣
# B = 11 台中市 K = 19 苗栗縣 T = 27 屏東縣
# C = 12 基隆市 L = 20 台中縣 U = 28 花蓮縣
# D= 13 台南市 M = 21 南投縣 V = 29 台東縣
# E = 14 高雄市 N = 22 彰化縣* W = 32 金門縣
# F = 15 台北縣* O = 35 新竹市 X = 30 澎湖縣
# G = 16 宜蘭縣 P = 23 雲林縣 Y = 31 陽明山
# H = 17 桃園縣 Q = 24 嘉義縣* Z = 33 連江縣
# I = 34 嘉義市 R = 25 台南縣
#(2)第一位數字則是拿來區分性別，男性為1、女性為2，
#驗證邏輯規則:
# (1)英文轉成的數字, 個位數乘９再加上十位數
# (2)各數字從右到左依次乘１、２、３、４．．．．８，做積之和
# (3)求出的積除10後之餘數,用10減該餘數,結果就是檢查碼,若餘數為0，檢查碼就是0　　　
id_rule_template = "^[A-Z]{1}[1-2]{1}[0-9]{8}$"
input_01=  "A123456789"
input_02=  "A122344567"
input_03=  "A986343244"


#(5)中文字
print("==================判斷中文字-======================")
input_01=  "0933123456"
input_02=  "中文字"
input_03=  "我是達人"
def  isChinese_Word(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

print(isChinese_Word(input_01))  #驗證失敗
print(isChinese_Word(input_02))  #驗證成功
print(isChinese_Word(input_03))  #驗證成功


#(6)英文
print("==================判斷全部英文字-======================")
word_rule_template = "^[A-Za-z]+$"
input_01=  "0933123456"
input_02=  "adbceer"
input_03=  "2134fddee"
print(re.fullmatch(word_rule_template,input_01))  #驗證失敗
print(re.fullmatch(word_rule_template,input_02))  #驗證成功
print(re.fullmatch(word_rule_template,input_03))  #驗證失敗

#(6)台灣統一編號
print("==================驗證台灣新版統一編號-======================")
#驗證邏輯公式:(含2023/4以後擴增)
#1、長度：共八位，，全部為數字型態。
#2、各數字分別乘以 1,2,1,2,1,2,4,1。
#3、當第 7 位數為 7 者，可取相加之倒數第二位取 0 及 1 來計算其和。
#4、假如其和能被 10 整除，則表示營利事業統一編號正確
#5、新制:修正統一編號之檢查邏輯由可被「10」整除改為可被「5」整除，預計自112年4月1日使用
#參考:https://slashview.com/archive2022/20221112.html
#
number_8_rule_template = "^[0-9]{8}$"

def isTax_Id_NumberForNewRule(input_str):
    multiply_array = [1,2,1,2,1,2,4,1]
    mutilply_sum=[-1,-1] 
    i=0
    for stra in input_str:
        isLucky_Sevent = False 
        num = int(stra)
        sub_sum = num * multiply_array[i]
        #print(str(i)+":"+str(sub_sum))
        if((sub_sum/10)>0):
           quotient = sub_sum//10
           remainder = sub_sum%10
           sub_sum = quotient+remainder
           #print(str(i)+":"+str(quotient)+","+str(remainder)+"="+str(sub_sum))
           if(i==6 and num==7 and sub_sum ==10): #第七位數等於7
                isLucky_Sevent = True
                #print("是否7:"+str(isLucky_Sevent))
        
        if isLucky_Sevent ==True:
            mutilply_sum[0] = mutilply_sum[0]+ 1
            mutilply_sum[1] = mutilply_sum[1]+ 0
        else:
            mutilply_sum[0] = mutilply_sum[0]+ sub_sum 
            mutilply_sum[1] = mutilply_sum[1]+ sub_sum 
        i = i+1
    mutilply_sum[0] = mutilply_sum[0]+ 1
    mutilply_sum[1] = mutilply_sum[1]+ 1

    print("第一位:{},第二位: {}".format(mutilply_sum[0],mutilply_sum[1]))
    #print(""+str((mutilply_sum[0]%5)))
    #print(""+str((mutilply_sum[1]%5)))
    #如果結果可以能被「5」整除表示為
    result = (mutilply_sum[0]%5==0) or (mutilply_sum[1]%5==0)
    #print("result:"+str(result))
    return result 
    
input_01=  "04595257"
input_02=  "10458575"
input_03=  "10458574"
input_04=  "12345678"
input_05=  "10458570"
print("input:"+input_01+",result:"+str(isTax_Id_Number(input_01)))
print("input:"+input_02+",result:"+str(isTax_Id_Number(input_02)))
print("input:"+input_03+",result:"+str(isTax_Id_Number(input_03)))
print("input:"+input_04+",result:"+str(isTax_Id_Number(input_04)))
print("input:"+input_05+",result:"+str(isTax_Id_Number(input_05)))





