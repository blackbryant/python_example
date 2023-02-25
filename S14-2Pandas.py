import pandas as pd 

#Series資料結構
se = pd.Series([1,2,3,4,5])
print("===========")
print(se)
print("===========")
print(se.values)
print("===========")
print(se.index)
print("===========")
print(se[2])
print("===========")
print(se[2:5])

se2 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(se2)
print(se2['a':'c'])

#使用字典建立Series
dic01 = {'Taipei':'台北',"Taichung":"台中","Kaohsiung":"高雄"}
se3 = pd.Series(dic01)
print(se3)
print(se3.index)
print(se3.values)
print(se3['Taipei'])
print(se3['Taipei':'Kaohsiung'])


#=========================================================
print("=========================DataFrame===========================")
#DataFrame 資料結構類似tables結構
df = pd.DataFrame([[66,65,64,63,62],
                   [56,55,54,53,52],
                   [46,45,44,43,42]])
print(df)

df2 = pd.DataFrame([[66,65,64,63,62],
                   [56,55,54,53,52],
                   [46,45,44,43,42]],
                   index=['王小明','李小美','陳大同'],
                   columns=['國文','英文','數學','自然','社會'])
print(df2)

#使用字典建立DataFrame
df3 = pd.DataFrame({'國文':{'王小明':65,'李小美':80,'陳大同':55},
                    '英文':{'王小明':90,'李小美':90,'陳大同':72},
                    '數學':{'王小明':50,'李小美':66,'陳大同':89},
                    '自然':{'王小明':80,'李小美':65,'陳大同':79},
                    '社會':{'王小明':78,'李小美':70,'陳大同':55}
                    })
print(df3)
#================================================================
#利用Series 建立DataFrame
se1 = pd.Series({'王小明':65,'李小美':80,'陳大同':55})
se2 = pd.Series({'王小明':90,'李小美':90,'陳大同':72})
se3 = pd.Series({'王小明':50,'李小美':66,'陳大同':89})
se4 = pd.Series({'王小明':80,'李小美':65,'陳大同':79})
se5  = pd.Series({'王小明':80,'李小美':65,'陳大同':79})
df4 = pd.concat([se1,se2,se3,se4,se5],axis=1)
df4.columns=['國文','英文','數學','自然','社會']
print(df4)
#取單筆資料
print(df4["國文"])
#取兩個以上的欄位
print(df4[["國文","英文"]])

