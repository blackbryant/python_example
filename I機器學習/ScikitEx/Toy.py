
# pip install scikit-learn
# pip install seaborn

from sklearn import datasets
import pandas as pd

'''
#Toy Datasets
ds = datasets.load_wine()
print(ds.DESCR)
df = pd.DataFrame(ds.data,columns=ds.feature_names)
print(ds.target)
print(ds.target_names)

x,y = datasets.load_wine(return_X_y=True)
print(x)
'''

#Real World Datasets
from sklearn.datasets import fetch_lfw_people
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#讀取70筆以上的人臉辨識，大小為40%
ds = fetch_lfw_people(min_faces_per_person=70,resize=0.4)
print(ds.images.shape)
n_simples,h,w = ds.images.shape
x=ds.data
y=ds.target
targe_names = ds.target_names
n_fetures = x.shape[1]
print(targe_names)
print(x)
nan_num = np.isnan(x).sum()
print("NAN number is : {nan_num} ".format(nan_num=nan_num))
df_y = pd.DataFrame({'code':y})
df_y["name"] = df_y["code"].map(dict(enumerate(ds.target_names)))
print(df_y["name"])

sns.countplot(x="name",data=df_y)
#plt.xticks(rotation=30)
plt.show()
#sns.set_theme()

X_train, X_test, y_train,y_test = train_test_split(x,y,test_size=.2)
print("=======train=======")
print(X_train,y_train)
print("=======test=======")
print(X_test,y_test)

#标准化数据，保证每个维度的特征数据方差为1，均值为0。使得预测结果不会被某些维度过大的特征值而主导
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)
#v訓練週期
clf = LogisticRegression(max_iter=500)
clf.fit(X_train_std,y_train)
y_pred = clf.predict(X_test_std)
print("=======y_pred=======")
print(y_pred)
print("=======X_test=======")
print(X_test)
# 评分函数
score = clf.score(X_test_std, y_test)
print(score)




