import numpy as np #numpy kütüphanesini dahil ettik

dizi = np.array([1,2,3,4,5,6,7,8]) #numpy dizisi oluşturduk. 1*8 yani bir boyutlu sekiz elemanlı matris aslında
print("Dizi elemanları: ",dizi)     #elemanları ekrana basar
print("Dizi tipi: ",type(dizi))     #dizi tipini gösterir.
print("kaça kaç matris: ",dizi.shape)  #kaça kaç bir matris olduğunu gösterir.şekil,biçim,form

print("-------------------------------------------------------------------")

d1 = dizi.reshape(2,4) #reshaper() diziyi 2(satır)*4(sütun) lük matris yapmamızı sağlar
print(d1)
print("sütun toplamı:",d1.sum(axis=0))
print("satır toplamı:",d1.sum(axis=1))
print("kaça kaç matris: ",d1.shape)     #kaça kaç matris olduğunu gösterir.
#print("matris kaç boyutlu: ", d1.ndim)       #kaç boyutlu olduğunu görürüz.
print("veri tipi: ",d1.dtype.name)      #matris hangi tür verilerden oluştuğunu gösterir.
print("kaç veri var: ",d1.size)         #dizide kaç veri olduğunu verir.
print("dizi tipi: ",type(d1))

print("-------------------------------------------------------------------")

sifir_dizi = np.zeros((3,3))        #sıfırlardan oluşan dizi yapar.
print(sifir_dizi)

sifir_dizi[0][0] = 5        #matrisin [0][0] elemanına değer atanır
print(sifir_dizi)

birler_dizi = np.ones((3,3))            #birlerden oluşan dizi yapar.
print(birler_dizi)

bos_dizi = np.empty((2,3))      #rastgele degerler atanmış dizi oluşturur.
print(bos_dizi)

d2 = np.arange(10,20,2)     #10 dan 20 ye kadar(20 dahil degil) aralarında 2 fark olan dizi oluşturur.
print(d2)

d3 = np.linspace(20,30,6)       #20 ve 30 arasında istenilen sayı kadar eleman oluşturur. 20 ve 30 dahil.
print(d3)

print("-------------------------------------------------------------------")

d4 = np.array([11,12,13])
d5 = np.array([7,8,9])

print("toplama: ",d4+d5) #toplama
print("çıkartma:",d4-d5)    #çıkartma
print("çarpma: ",d4*d5)    #çarpma
print("bölme: ",d4/d5)    #bölme
print("karesi: ",d4**2)    #karesini alma
print(np.sin(d4),np.sin(d5))    #sin değerleri
print(d4 < 5)   #elemanları 5ten küçük mü ? true veya false değer döndürür.
print("sqrt",np.sqrt(d4))       #karekökü alınır
print("square",np.square(d5))      #karesi alınır.
print(":",np.add(d4,d4))    #2 katını almayla aynı şey. iki matrisn toplamı

print("-------------------------------------------------------------------")

d6 = np.array(([[3,6,4],[2,0,7]]))
d7 = np.array(([[5,7,2],[9,4,1]]))

print(d6*d7)
#print(d6.dot(d7.T))
#print(np.exp(d6))

print("-------------------------------------------------------------------")

d8 = np.random.random((3,3))    #0 ile 1 arasında rastgele matris oluşturur.
print("random",d8)
print("toplam: ",d8.sum())     #matrisin toplam değeri
print("max: ",d8.max())     #matrisdeki en büyük sayi
print("min: ",d8.min())     #matrisdeki en küçük sayi

print(d8.sum(axis=0))       #sütunları toplar yeni matris yapar
print(d8.sum(axis=1))       #satırları toplar yeni matris yapar

print("-------------------------------------------------------------------")

d9 = np.array([[1,2,3,4],[5,6,7,8]])
print("0.eleman: ",d9[0])
# ters_cevir = d9[::-1]
# print("ters hali: ",ters_cevir)
print(d9[1:,:-1])
print(d9[1,:3])

print(d9.reshape(2,4))
d10 = d9.ravel()        #ravel matrisi tek boyuta indirir. vektör yapar yani
print(d10)
d10T = d9.T     #transpoz. satırla sütunun yerini değiştirir.
print(d10T)

print("-------------------------------------------------------------------")

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

array3 = np.column_stack((array1,array2)) #iki matrisi kolon olarak birleştirir.
array4 = np.row_stack((array1,array2))      #satır olarak yazar
array5 = np.vstack((array1,array2))     #veritical yukardakiyle aynı işlemi yapar sütun olarak birleştirir.
array6 = np.hstack((array1,array2))     #horizontal yatay
print(array3)
print(array4)
print(array5)
print(array6)

print("-------------------------------------------------------------------")

y = np.array([1,2,3,4,5])
o = y
l = y
print(y,o,l)
o[2] = 9        #burada y tek tanımlı obje olduğu için diğerleride y ye baglı oldugu için hepsi değişir.
print(y,o,l)

o = y.copy()
l = y.copy()        #kopyaladık ve hepsi birbirinden bağmsız oldu.
print(y,o,l)
o[2] = 15
print(y,o,l)

print("-------------------------------------------------------------------")