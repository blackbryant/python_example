#二位元檔案讀寫 待寫
#open(檔案名稱,[rwa]) 
#r:讀取模式，為預設模式
#w:寫模式
#a:附加模式
#close():關閉檔案
content=''' 這是一個檔案的寫入測試
#open(檔案名稱,[rwa]) 
#r:讀取模式，為預設模式
#w:寫模式
#a:附加模式      
'''

f = open("file.txt",'w')
f.write(content)

f.close()

with open("file.txt","r") as f:
    for line in f:
        print(line,end="")


#locale編碼模式
import locale
print(locale.getdefaultlocale())
with open("file.txt","r", encoding="cp950") as f:
    for line in f:
        print(line,end="")

#檔案處理
#flush():強迫將緩衝區的資料立即寫入檔案中
#readable():是否可以讀取
#read(n):讀取字元
#[]=readlines():回傳串列
print("=================readlines====================")
f = open("file.txt","r")
lines = f.readlines()
for line in lines:
    print(line,end="")
f.close()


#\ufeff是window系統用來辨識這是utf8的檔案，
print("=================BOM檔案====================")

with open("file_bom.txt","r",encoding="UTF-8") as f:
    doc = f.readlines()
    print(doc)

#1.使用notepad++儲存
#2.加上encoding="UTF-8-sig"
print("=================處理BOM檔案:UTF-8-sig====================")
with open("file_bom.txt","r",encoding="UTF-8-sig") as f:
    doc = f.readlines()
    print(doc)


#寫入
#writeable():是否可以寫入
#write(str):寫入
#writelines(list):串列寫入












