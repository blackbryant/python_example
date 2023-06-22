import pandas as pd

#利用Series 建立DataFrame
se1 = pd.Series({'王小明':65,'李小美':80,'陳大同':55})
se2 = pd.Series({'王小明':90,'李小美':90,'陳大同':72})
se3 = pd.Series({'王小明':50,'李小美':66,'陳大同':89})
se4 = pd.Series({'王小明':80,'李小美':65,'陳大同':79})
se5 = pd.Series({'王小明':90,'李小美':65,'陳大同':79})
df = pd.concat([se1,se2,se3,se4,se5],axis=1)
df.columns=['國文','英文','數學','自然','社會']

#資料排序
df2 = df.sort_values('國文',ascending=1)
print(df2)
print(df.sort_index(axis=1))
print(df.sort_index(axis=0))

#資料修改
df.loc['王小明']['數學']=90
df.loc['王小明'][:]=80

#刪除DataFrame資料
df.drop("王小明")
print(df)

#檔案存取
#CSV檔案
df2 = pd.read_csv("test1.csv",encoding='big5',header=0,index_col=0)
print(df2)
print(type(df2))

#html
#需要安裝 > pip install lxml
#keep_default_na 是否去除空白
url="https://www.tiobe.com/tiobe-index"
tables=pd.read_html(url,header=0,keep_default_na=False)
print(tables[0])

#寫入CSV檔案
df.to_csv("score3.csv",encoding='utf-8')
df.to_json("score3.json")

#sqlite
#sqlit_csv = pd.read_sql('aa.sqlite')


