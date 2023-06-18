'''
    有序:例如衣服尺寸S、M、L、XL
    無序:顏色 紅、藍、綠，性別(男、女)
'''

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder

#自訂類別變數
df = pd.DataFrame([['green','M',10.1,'class1'],
                   ['red','L',13.5,'class2'],
                   ['blue','XL',15.3,'class1']])

df.columns=["color","size","price","class-label"]
print(df)


#自訂index
size_mapping ={"XL":3,
               "L":2,
               "M":1}
df["size1"] = df["size"].map(size_mapping)
print(df) 

 #使用scikit-learn
data = [['Male',1],['Female',3],['Female',2]]
encoder = OrdinalEncoder()
print(encoder.fit_transform(data))





