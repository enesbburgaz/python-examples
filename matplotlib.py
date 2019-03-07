import pandas as pd
import matplotlib.pyplot as plt

veri = pd.read_csv('iris.csv') 

print(veri.columns)

print(veri.variety.unique()) 

print(veri.info())  

print(veri.describe())  


setosa = veri.iloc[50:100]   
setosa["id"] = range(0,50)
versicolor = veri.iloc[0:50] 
versicolor["id"] = range(0,50)
virginica = veri.iloc[100:150]
virginica["id"] = range(0,50)

print(setosa.describe())        
print(versicolor.describe())

print("-------------------------------------------------------------------")

plt.plot(setosa.id,setosa.petal_width,color="red",label="setosa")
plt.plot(versicolor.id,versicolor.petal_width,color="blue",label="versicolor")
plt.plot(virginica.id,virginica.petal_width,color="green",label="virginica")
plt.legend()    #plotta yazılan labeli grafiğin biryerine yazar
plt.xlabel("id")
plt.ylabel("petal_width")
plt.title("iris")
plt.grid()     
plt.show()

print("-------------------------------------------------------------------")
# %%
plt.hist(setosa.petal_width, bins=20)   
plt.xlabel("petal_width")              
plt.ylabel("frekans")
plt.grid()
plt.title("hist")
plt.show()

print("-------------------------------------------------------------------")
#%%
import numpy as np
milli_gelir = np.array([50,15,81,20,100,90])      
ulkeler = ["tr","usa","ger","rus","fr","italy"]
plt.bar(ulkeler,milli_gelir)
plt.xlabel("ulkeler")
plt.ylabel("milli_gelir")
plt.show()

print("-------------------------------------------------------------------")
#%% subplots

veri.plot(subplots=True)        .
plt.show()
plt.subplot(2,1,1)  #2tane grafik dedik
plt.plot(setosa.id,setosa.petal_width,color="red",label="setosa")  
plt.subplot(2,1,2)
#(2,1,1) = 2 tane satır 1 tane sutun içeren bir figure'ün 1. kısmına plot çizdir.
plt.plot(versicolor.id,versicolor.petal_width,color="blue",label="versicolor")
plt.show()





