#文字和位元

#範例一、用encode和decode互轉
s='Café'
print(len(s))
b = s.encode("utf8")  #轉成Bytes的編碼
print(len(b))         #有5個位元因為é轉成\xc3\xa9
print(b) 
c = b.decode("utf8")  #將bytes轉成字串
print(c)

#範例二、str和bytearray的切片操作会产生新的切片str和bytearry并拷贝数据
cafe = bytes('Café',encoding='utf8')
print(cafe)
print(cafe[2]) 
cafe_arr = bytearray(cafe) 
print(cafe_arr[-1:])           #bytearray 的slice還是bytearray

import array 
numbers = array.array('h',[-2,-1,0,1,2])  #建立16位元整數
octes = bytes(numbers)    
print(octes)

#使用struct进行unpack解析时可以直接接收memoryview对象，非常高效(避免大的str进行分段解析时大量的切片操作)。
import struct 
import os.path
import os
fmt='<3s3sHH'

current_directory = os.getcwd()
print(current_directory)
os.chdir(current_directory+os.sep+"流暢Python")
with open("zwj_sample.png",'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))
print(struct.unpack(fmt,header))
del header

del img

print("AAAAAAAAAAAAAA")
aa = memoryview(bytearray('abcdefg123',encoding='utf8'))
cc =struct.unpack(fmt,aa)
print(bytes(aa))


#編碼與解碼器
word_code_type = ['latin_1','utf8','utf16']

for codec in word_code_type: 
    print(codec,"São Paulo".encode(codec),sep="\t")

# cp437發生錯誤，排除例外但是看不出錯誤的地方
print("São Paulo".encode('cp437',errors="ignore"),sep="\t")
# cp437發生錯誤，用?代替
print("São Paulo".encode('cp437',errors="replace"),sep="\t")
# cp437發生錯誤，無法辨碼換成xml實體
print("São Paulo".encode('cp437',errors="xmlcharrefreplace"),sep="\t")


#UnicodeDecodeError
print("======UnicodeDecodeError======")
octets = b'Montr\xe9al'
print(octes.decode('cp1252'))
print(octes.decode("utf8",errors="replace"))

#big-endian or little-endian
u16le = 'El Nino'.encode("utf_16le")
print(list(u16le))
u16be = 'El Nino'.encode("utf_16be")
print(list(u16be))

