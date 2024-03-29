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
# pd.DataFrame(data, index, columns, dtype, copy)
#DataFrame 資料結構類似tables結構
df = pd.DataFrame([[66,65,64,63,62],
                   [56,55,54,53,52],
                   [46,45,44,43,42]])
print("===========DataFrame 資料結構================")
print(df)

print("===========單一list 建立================")
pd.DataFrame([1,2,3,4])
print(pd.DataFrame([['a','1'],['b','2'],['c','3']]))



#          '國文','英文','數學','自然','社會'
# 王小明     66,   65,    64,    63,   62
# 李小美     56,   55,    54,    53,   52
# 陳大同     46,   45,    44,    43,   42

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
#===============================================================\
print("==============新增欄位:加總=====================")
df3["加總"]=df3["國文"]+df3["英文"]+df3["數學"]+df3["自然"]+df3["社會"]
print(df3)

#===============================================================\
print("==============新增欄位:Insert=====================")
df3.insert(5,"體育",[60,60,70])
print(df3)

#===============================================================\
print("==============去除重複=====================")
data = [[1,2,3,4,5],
        [1,2,4,1,1],
        [1,2,3,4,5],
        [3,3,3,3,3],
        [5,5,5,5,5]]
df_data = pd.DataFrame(data) 
print(df_data.drop_duplicates())
#刪除所有重複
df_all_dup = df_data.drop_duplicates(keep=False)
print(df_all_dup)
#重製index
print(df_all_dup.reset_index())    

#===============================================================\
print("==============排序=====================")
data = [[1,2,3,4,5],
        [1,2,4,1,1],
        [1,2,3,4,5],
        [3,3,3,3,3],
        [5,5,5,5,5]]
df_order = pd.DataFrame(data,index=['a','e','c','b','d'],columns=["colA","colB","colC","colD","colE"]) 
print("==============標籤排序=====================")
print(df_order.sort_index())
print("==============反標籤排序=====================")
print(df_order.sort_index(ascending=False))
print("==============欄位排序=====================")
print(df_order.sort_index(axis=0))    
print(df_order.sort_index(axis=1))   

print("==============值排序=====================")
print(df_order.sort_values(by="colA"))    
print(df_order.sort_values(by=["colA","colC"]))   



#================================================================
#利用Series 建立DataFrame
se1 = pd.Series({'王小明':65,'李小美':80,'陳大同':55})
se2 = pd.Series({'王小明':90,'李小美':90,'陳大同':72})
se3 = pd.Series({'王小明':50,'李小美':66,'陳大同':89})
se4 = pd.Series({'王小明':80,'李小美':65,'陳大同':79})
se5 = pd.Series({'王小明':90,'李小美':65,'陳大同':79})
df4 = pd.concat([se1,se2,se3,se4,se5],axis=1)
df4.columns=['國文','英文','數學','自然','社會']
print(df4)
#取單筆資料
print(df4["國文"])
#取兩個以上的欄位
print(df4[["國文","英文"]])

#條件取值
# 國文大於80
print(df4[df4['國文']>=80])
#values 回傳二維陣列
print(df4.values)

#loc用欄位名稱來取得資料
#透過標籤索引
print("==============loc()=====================")

value1 = df4.loc["李小美",'英文']
print(value1)

#取出某部分資料集合
value2 = df4.loc["王小明":"李小美",'國文':'英文']
print(value2)

index_list=['王小明','李小美']
column_list=['國文','英文']
print(df4.loc[index_list,column_list])

#iloc用整數索引編號來取得資料
print("==============iloc()=====================")
print(df4.iloc[2,3])
print(df4.iloc[2,[1,2,3,4]])

#head([]):取的最前數列資料
print(df4.head(4))

#tail([]):取的最後數列資料
print(df4.tail(4))

#合併
print("==============合併()=====================")
left0 = pd.DataFrame({
                      'no': {'王小明':"0001",'李小美':"0002",'陳大同':"0003"},
                     '國文':{'王小明':65,'李小美':80,'陳大同':55},
                     '英文':{'王小明':90,'李小美':90,'陳大同':72}
                     
                    })

right0 = pd.DataFrame({
                     'no': {'王小明':"0001",'李小美':"0002",'陳大同':"0003"},
                    '數學':{'王小明':50,'李小美':66,'陳大同':89},
                    '自然':{'王小明':80,'李小美':65,'陳大同':79},
                    '社會':{'王小明':78,'李小美':70,'陳大同':55}
                    })
#print(left0)
#print(right0)

merge0 = pd.merge(left0,right0,on="no",sort=True)
print(merge0)

left1 = pd.DataFrame({
                      'no': {'王小明':"0001",'李小美':"0002",'陳大同':"0003","郭璽刀":"0004"},
                     '國文':{'王小明':65,'李小美':80,'陳大同':55,'郭璽刀':55},
                     '英文':{'王小明':90,'李小美':90,'陳大同':72,'郭璽刀':70},
                     '班級': {'王小明':"一年一班",'李小美':"一年一班",'陳大同':"一年二班",'郭璽刀':"一年二班"}
                    })

right1 = pd.DataFrame({
                     'no': {'王小明':"0001",'李小美':"0002",'陳大同':"0003","郭璽刀":"0004"},
                    '數學':{'王小明':50,'李小美':66,'陳大同':89,'郭璽刀':66},
                    '自然':{'王小明':80,'李小美':65,'陳大同':79,'郭璽刀':81},
                    '社會':{'王小明':78,'李小美':70,'陳大同':55,'郭璽刀':91},
                    '班級': {'王小明':"一年一班",'李小美':"一年一班",'陳大同':"一年二班",'郭璽刀':"一年二班"}
                    })
merge1 = pd.merge(left1,right1,on=["no","班級"],sort=True)
print(merge1)
# concat()
print("===========concat()=================")
a = pd.DataFrame({
    "A":["A0","A1","A2","A3"],
    "B":["B0","B1","B2","B3"],
    "C":["C0","C1","C2","C3"],
    "D":["D0","D1","D2","D3"],
})
b = pd.DataFrame({
    "A":["A4","A5","A6","A7"],
    "B":["B4","B5","B6","B7"],
    "C":["C4","C5","C6","C7"],
    "D":["D4","D5","D6","D7"],
})

print(pd.concat([a,b]))

print("===========append()=================")
c = a.append(b)
print(c)

print("===========Time line =================")
print(pd.Timestamp('2022-10-04'))
print(pd.Timestamp(1667573654,unit='s'))

#時間範圍
time_list = pd.date_range('9:00','18:00',freq='3min')
print(time_list)








