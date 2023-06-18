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
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer


df = sns.load_dataset('titanic')
print(df.head())

#欄位遺失值
isnull_sum = df.isnull().sum()
print(isnull_sum)

#中位數填補
#SimpleImputer
df.age.fillna(df.age.median(), inplace=True)


#平均數 mean 填補
imp = SimpleImputer(missing_values=np.nan, strategy="mean")
imp.fit([[1,2],[np.nan,3],[7,6]])
X=[[np.nan,2],[6,np.nan],[7,np.nan]]
print(imp.transform(X))

#中位數 median 填補
imp1 = SimpleImputer(missing_values=pd.NA, strategy="median")
#print(df.age.values)
#變成一行 以a行b列，相当于fit() + transform()
imp1.fit_transform(df.age.values.reshape(-1,1))

#大多數的人都會「直接移除資料」或是用「平均值來填補遺漏值」，但這樣的做法並不推薦：前者會讓資料減少，後者不會產生任何資訊。
#最推崇的就是「k-Nearest Neighbours」或「mice套件」來填補遺漏值。其中，mice的全名為Multivariate Imputation via Chained Equations。
#MICE多變數處理方式
imp = enable_iterative_imputer.IterativeImputer(max_iter=10,random_state=0)
imp.fit([[1,2],[3,6],[4,8],[np.nan,3],[7,np.nan]])
x_test = [[np.nan,2],[6,np.nan],[np.nan,6]]
print(imp.transform(x_test))
print(np.round(imp.transform(x_test)))


#pandas
df = sns.load_dataset('titanic')
df.sex = df.sex.map({'male':1,'female':0})
df2 = df[['pclass','sex','age','sibsp','parch','fare']]
imp = enable_iterative_imputer.IterativeImputer(max_iter=10,random_state=0)
df2= imp.fit_transform(df2.values)
df_new = pd.DataFrame(df2, columns=['pclass','sex','age','sibsp','parch','fare'])
print("============")
print(df_new.isnull().sum())

#前一筆替代遺失值
df[pd.isna(df.embark_town)]
df.embark_town.fillna(method='ffill',inplace=True)
print(df.loc[[61,829]])
print(df.loc[[61-1,829-1]])
