# 1) pandas hizli ve etkili for dataframes
# 2) csv ve text dosyalarÄ±na acip inceleyip sonuclarimiza bu dosya tiplerine rahat bir sekilde kaydedbilir.
# 3) pandas bizim isimizi kolaylastiriyor for missing data
# 4) reshape yapip datayi daha etkili bir sekilde kullanabiliriz
# 5) slicing indexing kolay
# 6) time series data analizinde cok yardimci
# 7) ayrica herseyden onemlisi hiz pandas hiz acisindan optimize edilmis hizli bir kutuphane

import pandas as pd      #data frame iÃ§in kullanÄ±lÄ±r.
import numpy as np

veri2 = pd.read_csv('iris.csv')

veri = {"isim":["ahmet","veli","mehmet","hasan"],"yas":[20,25,30,40]}

dt = pd.DataFrame(veri)     #excel gibi veri cercevesi yapmamÄ±zÄ± saÄlar

bas_kisim = dt.head()  #elimizdeki listenin ilk 5 satÄ±rÄ±nÄ± gÃ¶sterir default olarak (20) vs gibi yapabiliriz.

son_kisim = dt.tail() #son 5 satÄ±rÄ± gÃ¶sterir default olarak.


print("-------------------------------------------------------------------")

print(dt.columns)  # sÃ¼tun isimlerini verir.
print(dt.info())    #genel olarak dataframe hakkÄ±nda bilgi verir.
print(dt.dtypes)    #sÃ¼tunlarÄ±n tiplerini verir
print(dt.describe())    #dataframede ki numerik sÃ¼tunlar hakkÄ±nda basit mat iÅlemleri gÃ¶sterir. min,max,mean gibi.

print("-------------------------------------------------------------------")

print(dt["yas"])        #dataframede ki yas kolonunu yazdÄ±rÄ±r.
print(dt.yas)           #""

dt["maas"] = [150,250,350,450]   #yeni sÃ¼tun eklemek

#obje = pandasda string
# loc = strig ifadeler iÃ§im kullanÄ±lÄ±r. iloc = index iÅlemleri iÃ§in kullanÄ±lÄ±r
#indexing ve sliding
print(dt.loc[:,:"yas"]) #bastan yas sÃ¼tunu dahil yazar.
print(dt.loc[:,"isim":"maas"]) #isim ve yeni_sÃ¼tun dahil yazar
print(dt.loc[:,["isim","maas"]])  #sadece isim ve yeni_sÃ¼tunu yazar
print(dt.loc[::-1,:])      #satÄ±rlarÄ± tersten yazar

print(dt.iloc[:,1:3])   #1 ve 3 arasÄ±ndaki sÃ¼tunlarÄ± yazdÄ±rÄ±r. 3 dahil deÄildir.

print("-------------------------------------------------------------------")
#filtreleme
#bool = true veya false deÄeri alan Åeydir.

print(dt[dt.yas > 25])      #filtreleme iÅlemi
print(dt.yas > 25)      #boolÄ±n olarak ekrana bastÄ±rÄ±r.
filtre1 = dt.yas > 25
print(dt[dt.maas > 350])
print(dt.maas > 350)
filtre2 = dt.maas > 350
print(dt[filtre1 & filtre2])        #iki filtrenin birleÅtirilmesi

#filtreleme iki farklı filtreyi birleştirip yazma or veya not ilede yapılır.
data = veri2[np.logical_and(veri2['sepal_length'] > 5, veri2['petal_length'] > 5)]
#veya 
data2 = veri2[(veri2['sepal_length'] > 5) & (veri2['petal_length'] > 5)]

print("-------------------------------------------------------------------")
#list comprehension

ortalama_maas = dt.maas.mean()      #verilerin ortalamasÄ±nÄ± almak iÃ§in kullanÄ±lÄ±r.
print(ortalama_maas)

dt["maas_seviyesi"] = ["dusuk" if i < ortalama_maas else "yuksek" for i in dt.maas]
#maas, ortalama maas dan kÃ¼Ã§Ã¼kse yeni kolon aÃ§Ä±p dusuk veya yuksel Åeklinde yazar.

dt.columns = [i.upper() for i in dt.columns]    #kolon isimlerini lower veya upper ile bÃ¼yÃ¼ltÃ¼m kÃ¼Ã§Ã¼ltebiliriz.
print(dt.columns)

dt.columns = [i.split()[0]+"_"+i.split()[1] if (len(i.split()) > 1) else i for i in dt.columns]
#bu kod da eÄer boÅluk ile yazÄ±lmÄ±Å kolon baÅlÄ±ÄÄ± varsa onu bÃ¶lÃ¼p arasÄ±na _ koymamÄ±zÄ± saÄlar
print(dt)

print("-------------------------------------------------------------------")
#drop and concatenating

print(dt.drop(["MAAS_SEVIYESI"], axis=1))   #kolonu siler fakat inplace=true yapmassak gercek dataframe de uygulamaz
print(dt)                                   #bu satÄ±rda gÃ¶sterir sadece
print(dt.drop(["MAAS_SEVIYESI"], axis=1, inplace=True))
print(dt)

data1 = dt.head(1)
data2 = dt.tail(1)

data_concat = pd.concat((data1,data2),axis=0)       #birleÅtirme iÅine yarar.
print(data_concat)

data3 = dt.MAAS
data4 = dt.YAS
dt_concat = pd.concat((data3,data4),axis=0)     #satÄ±r olarak birÅeltirir.
print(dt_concat)

dt_concat = pd.concat((data3,data4),axis=1)     #sÃ¼tun olarak birleÅtirir.
print(dt_concat)

print("-------------------------------------------------------------------")
#transforming data

dt["apply_metodu"] = dt.MAAS.apply(lambda x:x*2)
print(dt)