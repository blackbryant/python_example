'''
#### 資料清理
* 清除HTML、合併、遺失值、離群值、資料型態轉換、統一格式
* 資料重複、重新命名
'''
'''
#### Missing value process
* 輸入漏打、收集設備故障
以鐵達尼號為例
'''
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

df = sns.load_dataset('titanic')
print(df.head())

#欄位遺失值
isnull_sum = df.isnull().sum()
print(isnull_sum)

#中位數
df.age.fillna(df.age.median(), inplace=True)

#平均數填補
imp = SimpleImputer(missing_values=np.nan, strategy="meam")
imp.fit([[1,2],[np.nan,3],[7,6]])

#轉換
X=[[np.nan,2],[6,np.nan],[7,6]]
print(imp.transform(X))





