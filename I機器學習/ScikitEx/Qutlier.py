'''
    離群值處理
    當資料實際狀態，大多數資料偏離很多，發生原因登打錯誤、資料蒐集設備故障等等，不可以刪除離群值，因為像迴歸
    會受影響很大
'''


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#離群值預測
#離群值偵測，從分析中檢測，並盡量刪除或解除離群值或遠離平均值的數據點，以防止任何潛在偏差的過程

def get_box_plot_data(labels, bp):
    row_line=[]
    for i in range(len(labels)):
        dict1={}
        dict1['label'] = labels[i]
        dict1['最小值'] = bp["whiskers"][i*2].get_ydata()[1]
        dict1['箱子下緣'] = bp["boxes"][i].get_ydata()[1]
        dict1['中位數'] = bp["medians"][i].get_ydata()[1]
        dict1['箱子上緣'] = bp["boxes"][i].get_ydata()[2]
        dict1['最大值'] = bp["whiskers"][i*2+1].get_ydata()[1]
        row_line.append(dict1)
    return pd.DataFrame(row_line)

df = sns.load_dataset('titanic')
print(df.head())
#如果有nan無法算出中位數，需要做前置處理
isnull_sum = df.isnull().sum()
print(isnull_sum)
df.age.fillna(df.age.median(), inplace=True)
bp=plt.boxplot(df.age)
#print(pd_box)
pd_box=get_box_plot_data(['age'],bp)

#plt.show()
#去除最大值與最小值
plt.clf()
df = df[(3.0<=df.age) & (df.age<=54.0)]
plt.hist(df.age)
plt.show()

#多維度使用DBScan或AutoEncoder等演算法



