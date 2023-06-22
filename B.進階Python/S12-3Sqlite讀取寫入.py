#Sqlite檔案存取
# 
#資料格式
# integer 整數
# real 浮點數
# text 文字檔
# blob 二進位
import sqlite3
conn = sqlite3.connect("aa.sqlite")
cursor = conn.cursor()
sql='''create table if not exists table01 \
("id" INTENGER PRIMARY  KEY NOT NULL,
"name" text not null,
"tel" text not null
)
'''
cursor.execute(sql)

data=[
    [3,'郭倖存','091234123423'],
    [4,'林志玲','093312342134']
]

# 新增資料表
try:
    for d in data:
        sql2 = "insert into table01 (id,name,tel) values ({},'{}','{}') "\
            .format(d[0],d[1],d[2])
        conn.execute(sql2)
except Exception as e:
    print(e)
finally:
    conn.commit()
    conn.close()

#更新資料
try:
    connet = sqlite3.connect("aa.sqlite")   
    connet.execute("UPDATE table01 SET name='{}' where id={}  "\
                .format('ken',1))
except Exception as e:
    print(e)
finally:
    connet.commit()
    connet.close()

#刪除
#DELET 資料表 where 
try:
    conn = sqlite3.connect("aa.sqlite")
    conn.execute("DELETE FROM table01 where id={} ".format(1))
except Exception as e:
    print(e)
finally:
    conn.commit()
    conn.close()

# drop 資料表
try:
    conn = conn.execute("DROP TABLE table01  ")
except Exception as e:
    print(e)
finally:
    conn.commit()
    conn.close()

#執行資料查詢
try:
    conn = conn.execute("select * from table01 ")
    rows = cursor.fetchall()
except Exception as e:
    print(e)
finally:
    conn.commit()
    conn.close()

try:
    conn = conn.execute("select * from table01 ")
    row = cursor.fetchone()
except Exception as e:
    print(e)
finally:
    conn.commit()
    conn.close()

