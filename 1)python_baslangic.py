#Python başlangıç = help(int,str,list..) şeklinde veya print(dir(..)) şeklinde bulamadığınız şeylere detaylı bakabilirsiniz.
#değisken tanımlama
#degiskenlerin  buyuk harfle baslamasi uygun degil ama yazılabilir tabiki
#5sayi şeklinde sayı başta tanımlanamaz.
sayi = 10  #int = integer
isim = "string" #str = string
flt = 10.1 #float
liste = [1,2,3,4,5,6,7,8,9] #list
dic = {"marka":"ford","model":"mustang","yıl":"1964"} #dictionary
tpl = ("elma","muz","kiraz") #tuple

# %% - %% şeklinde bölümleri ayırabiliriz.
#--------------------------------------------------------------------------------------
#kullanıcıdan veri alma
veri = input("Bir sayi giriniz: ")
print(veri)
#int(input(...)), str(input(...)), float(input(...)) şeklinde tip dönüşümleri yapabiliriz.

#verileri ekrana bastırma
print("#verileri ekrana bastırma")
print(sayi, isim, flt, liste, dic, tpl)
#değişenin tipi
print(type(sayi), type(isim), type(flt), type(liste), type(dic), type(tpl))
#verilerin uzunlukları
print(len(str(sayi)), len(isim), len(str(flt)), len(liste), len(dic), len(tpl))
# str(..), int(..), float(..) = tip değiştirme.
#--------------------------------------------------------------------------------------
#dört işlem
print("#dört işlem")
d1 = "istanbul"
d2 = "izmir"
print("d1 + d2: ",d1+d2)

#örnek 2 #str ifalerin toplanması, birleştirilmesi demek.
d3 = "100"
d4 = "200"
print("d3 + d4: ",d3+d4)

#örnek 3
d5 = 5
d6 = 7
print("Toplama: ",d5+d6, "Çıkarma: ",d5-d6, "Bölme: ",d5/d6, "Çarpma: ",d5*d6)

#örnek 4
yuvarla = 50.6
print(round(yuvarla))
#--------------------------------------------------------------------------------------
#index işlemleri
print("#index işlemleri")
print(isim[0]+"-",isim[1]+"-",isim[2]+"-", isim[3],isim[4]+"-",isim[5])
print(isim[:3]) #baştan 3'e kadar.3 dahil değil.
print(isim[3:])
print("5.sayı kacinci sirada: ",liste.index(5))
#[-1] --> listenin son elemanını alır.
#--------------------------------------------------------------------------------------
#liste işlemleri
print("#liste işlemleri")
liste2 = [10,20,30,40]
liste2.append(50) #listeye veri ekleme
print(liste2)
liste2.reverse() #listeyi ters çevirme
print(liste2)
liste2.remove(10) #listeden veri silme
print(liste2)
liste.sort(reverse=True) #listeyi tersine sıralar .sort() yaparsak normal sıralar.
print(liste)
#--------------------------------------------------------------------------------------
#tuple işlemleri
print("#tuple işlemleri")
print(tpl.count("elma"))    #elmadan tupleda kaçtane olduğunu gösterir.
print(tpl.index("muz"))     #muzun kaçıncı sırada olduğunu gösterir.
#--------------------------------------------------------------------------------------
#koşullar: if-elif-else
print("#koşullar: if-elif-else")
a,b = 3,4 # a = 3 , b = 4 şeklinde de ayrı ayrı tanımlanabilir.
if a > b:
    print("a sayisi büyük: ",a)
elif a == b:
    print("eşit")
else:
    print("b sayisi büyük: ",b)

#örnek 2
ara = 5
if ara in liste:
    print("{} sayisi listede var".format(ara)) #yazdırmak istediğimiz değeri dışardan .format(deger) şeklinde girebiliriz.
else:
    print("{} sayisi listede yok".format(ara))

#örnek 3
if "ford" in dic.values(): #dic.keys anahtarlar ve dic.values degerler olarak tanımlıdır.
    print("ford marka araba var")
else:
    print("ford marka araba yok")
#--------------------------------------------------------------------------------------
#döngüler: for-while
print("#döngüler: for")
for i in range(0,10): #0 dan 9 a kadar sayıları döndürür.
    print(i)

#örnek 2
for i in "istanbul izmir": #harf harf ekrana basar.
    print(i)

#örnek 3
for i in "istanbul,izmir".split(","): #belirttiğimiz şekilde böler. split() = boşluktan ,split("-") = - ile böler
    print(i)

#örnek 4 listedeki elemanları toplama
topla = 0
for i in liste:
    topla += i #topla = topla + i
print(topla)
#döngüsüz toplama
topla2 = sum(liste)
print(topla2)

#örnek 5 listedeki en büyük sayıyı bulma
k = 0
for t in liste:
    if k < t:
        k = t
print("En büyük sayi: ",k)
#döngüsüz en büyük sayıyı bulma
mini = min(liste)
maxi = max(liste)
print("min sayi: ",mini,"max sayi: ",maxi)

print("#döngüler: while")
w = 0
while(w < 4):
    print(w)
    w += 1

#örnek 2 listedeki sayiları toplama
ust_deger = len(liste)
topla3 = 0
d = 0
while(d < ust_deger):
    topla3 += liste[d]
    d += 1
print(topla3)
#--------------------------------------------------------------------------------------