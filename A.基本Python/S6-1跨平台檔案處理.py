#Shutil模組:跨平台模組，
#
#
import shutil

#copy(來源檔案,目的檔案)、copyfile(來源檔案,目的檔案)
#shutil.copy("S6-1跨平台檔案處理.py","S6-1跨平台檔案處理_copy.py")

#copytree(來源目錄,目的目錄):複製目錄與使目錄
#retree(來源目錄,目的目錄):刪除空的目錄，和刪除指定目錄與目錄的子目錄和檔案
#shutil.copytree("E:\\testaa","C:\\testaa")


#glob模組: 查詢目錄下的檔案，利用*字元可以列出檔案
import glob
search_files = glob.glob("S2-1_數值.py") + glob.glob("S3*.py")
for file in search_files:
    print(file)
