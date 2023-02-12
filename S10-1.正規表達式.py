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

#match()：回傳MatchObject物件
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

print("======findall========")
temp="anmc1234asdfdf"
rule_a=re.compile(r"[a-z]+")
m = rule_a.findall(temp)
print(m,end=",\r\n")










