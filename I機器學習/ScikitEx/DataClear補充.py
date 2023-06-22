import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
X = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
X1 = np.array([[1, 2, np.nan],
               [4, np.nan, 6],
               [np.nan, 8, 9]])
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(X)
print(imp.transform(X1))
#[[1. 2. 6.]
# [4. 5. 6.]
# [4. 8. 9.]]
