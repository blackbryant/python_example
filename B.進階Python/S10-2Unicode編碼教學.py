#
#
#
#
#

#編碼café
s= 'café'
print("len:"+str(len(s)))

#b'caf\xc3\xa9' 其中b表示為byte
b= s.encode("utf8")
print(b)

#編碼caf\xc3\xa9->café
print(b.decode())

#16進位建構二進制
s="31 48 CE A9"
print(bytes.fromhex(s))










