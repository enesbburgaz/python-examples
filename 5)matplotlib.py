# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt

veri = pd.read_csv('iris.csv')  #veriyi dışardan dahil etme

print(veri.columns)

print(veri.variety.unique()) #variety kolonunda kaç varklı veri olduğunu buluruz.

print(veri.info())  #veri kümesi hakkında bilgi verir.

print(veri.describe())  #veriler hakkında bilgi verir.


setosa = veri.iloc[50:100]    #setosa türünü data dan ayırmış olduk
setosa["id"] = range(0,50)
versicolor = veri.iloc[0:50] #versicolor "
versicolor["id"] = range(0,50)
virginica = veri.iloc[100:150]
virginica["id"] = range(0,50)

print(setosa.describe())        #iki veriyi karşılaştırıp veri hakkında bilgi edinebiliriz.
print(versicolor.describe())

print("-------------------------------------------------------------------")

plt.plot(setosa.id,setosa.petal_width,color="red",label="setosa")   #scatter da kullanılır noknalı gösterir.
plt.plot(versicolor.id,versicolor.petal_width,color="blue",label="versicolor")
plt.plot(virginica.id,virginica.petal_width,color="green",label="virginica")
plt.legend()    #plotta yazılan labeli grafiğin biryerine yazar
plt.xlabel("id")
plt.ylabel("petal_width")
plt.title("iris")
plt.grid()      #alpha =  de saydamlığı ayarlar.
plt.show()

print("-------------------------------------------------------------------")
# %%
plt.hist(setosa.petal_width, bins=20)   #hangi veride kaç tane oldugunu grafik şeklinde
plt.xlabel("petal_width")               #ekrana basar. bins histogramın kalınlığını ayarlar.
plt.ylabel("frekans")
plt.grid()
plt.title("hist")
plt.show()

print("-------------------------------------------------------------------")
#%%
import numpy as np
milli_gelir = np.array([50,15,81,20,100,90])        #verilerin kaça karşılık geldiğini görebiliriz.
ulkeler = ["tr","usa","ger","rus","fr","italy"]
plt.bar(ulkeler,milli_gelir)
plt.xlabel("ulkeler")
plt.ylabel("milli_gelir")
plt.show()

print("-------------------------------------------------------------------")
#%% subplots

veri.plot(subplots=True)        #tek grafikte farklı grafikler gibi gösterir.
plt.show()
plt.subplot(2,1,1)  #2tane grafik dedik
plt.plot(setosa.id,setosa.petal_width,color="red",label="setosa")   #scatter da kullanılır noknalı gösterir.
plt.subplot(2,1,2)
#(2,1,1) = 2 tane satır 1 tane sutun içeren bir figure'ün 1. kısmına plot çizdir.
plt.plot(versicolor.id,versicolor.petal_width,color="blue",label="versicolor")
plt.show()





