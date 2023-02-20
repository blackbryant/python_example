#Sqlite檔案存取
# 
#資料格式

import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='test',charset="utf8",db="test")

#刪除
with conn.cursor() as cursor:
    delete_data=[3,4]
    for d in delete_data: 
        delete_sql ="DELETE FROM db_name where id={}".format(d)
        cursor.execute(delete_sql)
        conn.commit()


#新增資料
with conn.cursor() as cursor:
    insert_data=[
    [3,'郭倖存',10.0,'test1'],
    [4,'林志玲',10.0,'test2']
    ]

    for d in insert_data:
        sql="INSERT INTO db_name (id, name, price, mone) VALUES ({},'{}',{},'{}')".format(d[0],d[1],d[2],d[3])
        cursor.execute(sql)
        conn.commit()
    
#查詢
with conn.cursor() as cursor:
    sql="SELECT * FROM db_name "
    cursor.execute(sql)
    datas= cursor.fetchall()
    print(datas)
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)

conn.close()



