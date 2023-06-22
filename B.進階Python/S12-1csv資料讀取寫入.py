#CSV檔案存取
#
#一維陣列
import csv
with open('test1.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['姓名','身高','體重'])
    writer.writerow(['chiou',170, 65])
    writer.writerow(['David',183, 78])

#二維陣列
csvtable=[
    ['姓名','身高','體重'],
    ['chiou',170, 65],
    ['David',183, 78]
    ]
with open('test2.csv','w',newline='') as csvfile:
    writer = csv.writer(csvtable)
    writer.writerow(csvtable)

#字典資料寫入檔案
with open('test.csv','w',newline='') as csvfile:
    fieldnams=['姓名','身高','體重']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnams)
    writer.writeheader()
    writer.writerow({'姓名':'Chios','身高':170,'體重':65})
    writer.writerow({'姓名':'David','身高':183,'體重':78})


with open('test2.csv','w',newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(row)    



