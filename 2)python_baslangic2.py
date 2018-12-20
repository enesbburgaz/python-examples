#fonksiyonlar
print("#fonksiyonlar")
def fonk(): #geriye değer döndürmeyen fonksiyon
    print("Fonksiyonum")

fonk() #fonksiyon çağırılır.

#örnek 2
def fonk2(x):   #geriye değer döndüren fonksiyon
    return x*x

print(fonk2(5)) #fonksiyona değer gönderilir.
#--------------------------------------------------------------------------------------
#default fonksiyonlar
print("#default fonksiyonlar")
def fonk3(x,y,z=10): #default olarak tanımlanan parametre sona yazılır.
    return (x*y)/z

print(fonk3(6,5))
#--------------------------------------------------------------------------------------
#*args kullanımı
print("#*args kullanımı") #Tuple olarak ifade edilen veri tipidir.illa *args değil *deneme,*a,*b gibi kullanılabilir.
def fonk4(a,b,*args):   #daha sonra parametre tanımlamamak için args'ı kullanabiliriz.
    print("degiskenler: ",a,b)
    print("args:",*args)
    print("args:",args, ", tip:",type(args))
    print("args0:",args[0], ", tip:",type(args[0]), "args2:",args[2], ", tip:",type(args[2]))

fonk4(4,5,6,8,"isim",10)
#--------------------------------------------------------------------------------------
#**kwargs kullanımı
print("#**kwargs kullanımı") #Dictionary olarak ifade edilen veri tipidir.illa *kwargs değil **deneme,**a,**b gibi kullanılabilir.
def fonk5(**kwargs):
    for anahtar, deger in kwargs.items(): #.keys(), .values() .. gibi
        print("Anahtar: {0}, Değer: {1}".format(anahtar,deger))

fonk5(fiat = "egea", mercedes = "c180", bmw ="m5")
#--------------------------------------------------------------------------------------
#lambda fonksiyonu
print("#lambda fonksiyonu")
def fonk6(x):
    return x*x
print(fonk6(9))

fonk7 = lambda x: x*x
print(fonk7(9))
#--------------------------------------------------------------------------------------
#sınıflar
print("#sınıflar")
class otomobil:
    km = 100
    oto_sayisi = 0
    def __init__(self,seri,model,yil,yakit,renk):   #sınıf içinde ilk çalışacak metot
        self.oto_seri = seri
        self.oto_model = model
        self.oto_yil = yil              #self bizim istediğimiz, gönderdiğimiz obje için işlem yapar.
        self.oto_yakit = yakit
        self.oto_renk = renk
        self.oto_km = otomobil.km
        otomobil.oto_sayisi += 1
    def bastir(self):
        return self.oto_seri+" "+self.oto_model+" "+self.oto_yil+" "+self.oto_yakit+" "+self.oto_renk+" "+str(self.oto_km)
    #otomobillerin tüm özelliklerini return ile döndürüp görürüz.
bmw = otomobil("5 Serisi","520d","2016","Dizel","Beyaz") #oluşturduğumuz objeler
mercedes = otomobil("E Serisi","E250","2011","Dizel","Siyah")

print(bmw.bastir())
print(mercedes.bastir())
bmw.oto_km = 500
mercedes.oto_renk = "Lacivert"
print(bmw.bastir())
print(mercedes.bastir())
print("Otomobil sayisi: ",otomobil.oto_sayisi)

liste = [bmw,mercedes]   #objeleri listeye attık
max_km = 0
index = 0
for i in liste: # i listenin içindeki objeler oluyor.
    if max_km < i.oto_km:   #i.oto_km yi bmw.oto_km olarak düşünebiliriz
        max_km = i.oto_km
        index = i   # index = i nin içinde ne varsa . index = mercedes

print("En yüksek kilometre:",max_km, "Kim:",index.bastir())
#--------------------------------------------------------------------------------------