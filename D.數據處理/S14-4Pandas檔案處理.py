import pandas as pd
#

print("===========to_csv=========")

df2 = pd.read_csv("test1.csv",encoding='big5',header=0,index_col=0)
print(df2)
print(type(df2))
















