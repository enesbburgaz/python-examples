import pandas as pd
import numpy as np

veri2 = pd.read_csv('iris.csv')

veri = {"isim":["ahmet","veli","mehmet","hasan"],"yas":[20,25,30,40]}

dt = pd.DataFrame(veri)     

bas_kisim = dt.head()  

son_kisim = dt.tail() 


print("-------------------------------------------------------------------")

print(dt.columns)  
print(dt.info())   
print(dt.dtypes)    
print(dt.describe())   

print("-------------------------------------------------------------------")

print(dt["yas"])
print(dt.yas)          

dt["maas"] = [150,250,350,450]   

#indexing ve sliding
print(dt.loc[:,:"yas"]) 
print(dt.loc[:,"isim":"maas"]) 
print(dt.loc[:,["isim","maas"]])  
print(dt.loc[::-1,:])     

print(dt.iloc[:,1:3])  

print("-------------------------------------------------------------------")

print(dt[dt.yas > 25])     
print(dt.yas > 25)      
filtre1 = dt.yas > 25
print(dt[dt.maas > 350])
print(dt.maas > 350)
filtre2 = dt.maas > 350
print(dt[filtre1 & filtre2])        

#filtreleme iki farklı filtreyi birleştirip yazma or veya not ilede yapılır.
data = veri2[np.logical_and(veri2['sepal_length'] > 5, veri2['petal_length'] > 5)]
#veya 
data2 = veri2[(veri2['sepal_length'] > 5) & (veri2['petal_length'] > 5)]

print("-------------------------------------------------------------------")
#list comprehension

ortalama_maas = dt.maas.mean()   
print(ortalama_maas)

dt["maas_seviyesi"] = ["dusuk" if i < ortalama_maas else "yuksek" for i in dt.maas]

dt.columns = [i.upper() for i in dt.columns]    
print(dt.columns)

dt.columns = [i.split()[0]+"_"+i.split()[1] if (len(i.split()) > 1) else i for i in dt.columns]
print(dt)

print("-------------------------------------------------------------------")
#drop and concatenating

print(dt.drop(["MAAS_SEVIYESI"], axis=1))  
print(dt)                                  
print(dt.drop(["MAAS_SEVIYESI"], axis=1, inplace=True))
print(dt)

data1 = dt.head(1)
data2 = dt.tail(1)

data_concat = pd.concat((data1,data2),axis=0)       
print(data_concat)

data3 = dt.MAAS
data4 = dt.YAS
dt_concat = pd.concat((data3,data4),axis=0)  
print(dt_concat)

dt_concat = pd.concat((data3,data4),axis=1)  
print(dt_concat)

print("-------------------------------------------------------------------")
#transforming data

dt["apply_metodu"] = dt.MAAS.apply(lambda x:x*2)
print(dt)