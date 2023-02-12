#目錄與檔案
#OS模組
import os
#getcwd : 取得目前工作目錄
print(os.getcwd())

#exist:檢查檔案是否存在
print(os.path.exists(os.getcwd()))

#remove:
rm_file ="text.txt"
if os.path.exists(rm_file):
    os.remove(rm_file)
else:
    print("找無檔案")

#mkdir:建立目錄資料夾
new_dir = "test" 
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
else:
    print("找無檔案")

#rmdir:刪除指定目錄
if os.path.exists(new_dir):
    os.rmdir(new_dir)
else:
    print("目錄未建立")

#system:執行consle的指令
#os.system("cls")
#os.system("mkdir dir2")
#os.system("notepad "+ "S6-1檔案系統.py")

########################################
#os.path模組
#abspath(filename):回傳完整的檔案路徑
#getsixe(filename):回傳大小bytes
filename1=os.path.abspath("S5-4骰子遊戲.py")
if os.path.exists(filename1):
    print(filename1+"檔案存在")
    print("大小:"+str(os.path.getsize(filename1)))

#dirname(filename):__file__回傳目前目錄
print(os.path.dirname(__file__))

#join([字串]):將字串連結一個檔案路徑
join_path1= os.path.join("E:\TAILWIND","\\","tailwind介紹.txt")
isDir = os.path.isdir(join_path1)
print(join_path1) 
print(isDir) 
#slpit()分解為目錄與檔案
adir,afilename= os.path.split(join_path1)
print("目錄:"+adir,"檔案:"+afilename)

# (目錄名稱,下一層目錄層級,目錄中所有檔案串列)=os.walk函式走訪子目錄
#
#
cur_path = os.path.dirname(__file__)
print("目前目錄:",cur_path)
tree = os.walk(cur_path)
for dirname,subdir,files in tree:
    print("檔案路徑:",dirname)
    print("目錄串列:",subdir)
    print("檔案串列:",files)
    print()




