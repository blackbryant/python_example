#S5-3字串函式
word="book"

#字串置中:string.center(n)
print(word.center(8))

#搜尋字串的Index:find(w)
print(word.find('o'))

#以S字串為結尾: string.endswith(s)
print(word.endswith("k"))

#islower() , isupper()
print(word.islower())

#以字串為連結: word.join(list)
print(",".join(["A","B"]))
 
 # lstrip:去除左方的空白字元
 # rstrip:去除右方的空白字元
 # strip:兩邊空白字元
message_a = " I can help  "
print(message_a.lstrip()) 
print(message_a.rstrip())
print(message_a.strip())
 
#string.find:搜尋字串
print(message_a.find("help"))

#string.replace
print(message_a.replace(" ", "&")) #&I&can&help&&
print(message_a.replace(" ", "&",1)) #&I can help

#日期轉換
date1="2023-01-01"
date1 = date1.replace("-","年",1)
date1 = date1.replace("-","月",1)
date1 +="日"
print(date1)
