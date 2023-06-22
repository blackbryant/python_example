#正規表達式
#語法檢查：https://pythex.org/
'''
中介字元	說明
.	除了新行符號外的任何字元，例如 '.' 配對除了 '\n' 之外的任何字元。
^	字串開頭的子字串或排除指定字元或群組，例如 'a[^b]c' 配對除了 'abc' 之外的任何 a 開頭 c 結尾的三字元組合。
$	字串結尾的子字串，例如 'abc$' 配對以 'abc' 結尾的字串。
*	單一字元或群組出現任意次數，例如 'ab*' 配對 'a' 、 'ab' 或 'abb' 等等。
+	單一字元或群組出現至少一次，例如 'ab+' 配對 'ab' 或 'abb' 等等。
?	單一字元或群組 0 或 1 次，例如 'ab+' 配對 'a' 或 'ab' 。
{m,n}	單一字元或群組的 m 到 n 倍數，例如 'a{6}' 為連續六個 'a' ， 'a{3,6}' 為三到六個 'a' 。
[]	對中括弧內的字元形成集合，例如 '[a-z]' 為所有英文小寫字母。
\	特別序列的起始字元。
|	單一字元或群組的或，例如 'a|b' 為 'a' 或 'b' 。
()	對小括弧內的字元形成群組。
\number	群組的序數
\A	字串的開頭字元。
\b	作為單字的界線字元，例如 r'\bfoo\b' 配對 'foo' 或 'bar foo baz' 。
\B	作為字元的界線字元，例如 r'py\B' 配對 'python' 或 'py3' 。
\d	數字，從 0 到 9 。
\D	非數字。
\s	各種空白符號，包括新行符號 \n 。
\S	非空白符號。
\w	任意文字字元，包括數字。
\W	非文字字元，包括空白符號。
\Z	字串的結尾字元。
'''

#match()：只要第一個字元不符合，就會結束搜尋，回傳None，如果有找到就會回傳MatchObject物件
#(r"[a-z]+" 加上r防止表達中有\ 跳脫字元 
import re
temp="temp12po"
rule_a=re.compile(r"[a-z]+")
m = rule_a.match(temp)
if not m ==None:
    print(m.group())#temp
    print(m.start())#0
    print(m.end())  #3
    print(m.span()) #回傳起,迄

#search():傳回指定定義第一組符合正規劃表達字串
print("===== search搜尋=========")
temp="1234temp1234"
rule_a=re.compile(r"[a-z]+")
m = rule_a.search(temp)
if not m ==None:
    print(m.group())#temp
    print(m.start())#0
    print(m.end())  #3
    print(m.span()) #回傳起,迄  

#findall():找出字串所有符合的正規表達式。
print("======findall========")
temp="anmc1234asdfdf"
rule_a=re.compile(r"[a-z]+")
m = rule_a.findall(temp)
print(m,end=",\r\n")


#分組方式
#
print("=================group=========================")
phone_num="tel:02-12345678"
phone_rule=r"(\d{2})-(\d{8})"
phone = re.search(phone_rule,phone_num)
if not phone ==None:
    print("共幾個{}Group".format( len(phone.groups())))
    print(phone.group())
    print(phone.group(0))
    print(phone.group(1))
    print(phone.group(2))
     

# "?" 搜尋:字元出現1次或0次，該字元可有可無
print("=================????=========================")
phone_num="tel:0212345678"
phone_rule=r"(\d{2})-?(\d{8})"
phone = re.search(phone_rule,phone_num)
if not phone ==None:
    print("共幾個{}Group".format( len(phone.groups())))
    print(phone.group())
    print(phone.group(0))
    print(phone.group(1))
    print(phone.group(2))

# "|" 搜尋:同時比對多個格式
'''
print("=================||||=========================")
phone_nums=["tel:0212345678","tel:(02)-12345678","tel:049-12345678","tel:0933-123456","tel:04-12345678"]
phone_rule=r"(\d{2})-?(\d{8})|(\d{4})-?(\d{6})"
phones = re.search(phone_rule,phone_nums)
i=1
for phone in phone_nums:
    num = re.search(phone_rule,phone)
    if not num==None:
        print("===>"+i)
        print("共幾個{}Group".format( len(phone.groups())))
        print(phone.group())
        #print(phone.group(0))
        #print(phone.group(1))
        #print(phone.group(2))
'''    

# 字元分類
#
print("===============字元分類=================")
rule_b = r'[0-9+]+'
s = "Amy was 18 year old, she like dog."
m = re.findall(rule_b,s)
print(m)

# 使用+字元搜尋
#
print("===============+=================")
rule_c= r'[aeiou]+'
s="John is my best friend"
m=re.findall(rule_c,s)
print(m)

# 使用忽略大小字元
#
a01=r'PYTHON|ANDROID'
s = r'I like Python and Android! '
m1= re.findall(a01,s,re.I)
print(m1)

# 使用^字元
#

print("========================================================")





