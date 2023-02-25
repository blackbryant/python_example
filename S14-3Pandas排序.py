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