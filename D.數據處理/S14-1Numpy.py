#numpy
#使用多維陣列取代python的串列資料，
#
#一維陣列

import numpy as np
np1 = np.array([1,2,3,4])
np2 = np.array([5,6,7,8])
print(np1)
print(np2)
print(type(np1),type(np2))

na = np.array([1,2,3,4], dtype=int)

#arange
np2 = np.arange(0,31,2)
print(np2)

#等距陣列
np3 = np.linspace(1,15,3)
print(np3)

#zeros()、ones()
zeros = np.zeros(5)
print(zeros)
ones = np.ones(5)
print(ones)

#empty()建立隨機陣列
c = np.empty((2,5))
print(c)


#============================建立多維陣列======================
adata = np.arange(1,17)
bdata = adata.reshape(4,4)
print(bdata)










