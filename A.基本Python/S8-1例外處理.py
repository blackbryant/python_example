#例外處理
#當程式執行發生例外，例如：整數除以0、檔名不存在等等，應該是處理例外處理狀況發生
#而是中斷程式執行
#說明：https://docs.python.org/zh-tw/3/tutorial/errors.html
#try...except...else...finally
#NameError		    使用沒有被定義的對象
#IndexError		    索引值超過了序列的大小
#TypeError		    數據類型 ( type ) 錯誤
#SyntaxError		Python 語法規則錯誤
#ValueError		    傳入值錯誤
#KeyboardInterrupt	當程式被手動強制中止
#AssertionError		程式 asset 後面的條件不成立
#KeyError		    鍵發生錯誤
#ZeroDivisionError	除以 0
#AttributeError		使用不存在的屬性
#IndentationError	Python 語法錯誤 ( 沒有對齊 )
#IOError		Input/output異常
#UnboundLocalError	區域變數和全域變數發生重複或錯誤
def devide(a,b):
    return a/b

try:
    print(devide(10,2))
    print(devide(10,0))
except ZeroDivisionError as zde:
    print(zde)
except Exception as e:
    print(e)
finally:
    print("=>一定執行的區塊")


#捕抓多個例外
try:
    print(devide(10,2))
    print(devide(10,0))
except (ZeroDivisionError,Exception) as e:
    print(e)
finally:
    print("=>一定執行的區塊")

#(2) raise
#函式中拋出例外訊息
#
def CheckDevide(a1,a2):
    if(a2==0):
        raise Exception("除以相除發生錯誤")
    result = a1/a2
    return  result

for num in [10,20,0]:
    a1=20
    try: 
        result=CheckDevide(a1,num)
        print("分子:{},分母:{},結果:{}".format(a1,num,result))
    except Exception as e:
        print("分子:{},分母:{},錯誤:{}".format(a1,num,e))


#拋出自訂例外
print("=============自訂例外===============")
class MyException(RuntimeError):
    def __init__(self, arg) :
        self.arg =arg

def CheckDevideWithMyException(a1,a2):
    if(a2==0):
        raise MyException("自訂例外，除以相除0發生錯誤")
    result = a1/a2
    return  result

for num in [10,20,0]:
    a1=20
    try: 
        result=CheckDevideWithMyException(a1,num)
        print("分子:{},分母:{},結果:{}".format(a1,num,result))
    except MyException as e:
        print("分子:{},分母:{},錯誤:{}".format(a1,num,e))

#紀錄例外字串
#Traceback紀錄字串
import traceback
for num in [20,10,0]:
    try:
        CheckDevide(20,num)
    except Exception as e:
        print(traceback.format_exc())
    

