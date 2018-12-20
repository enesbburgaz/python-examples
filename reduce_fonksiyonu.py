from functools import reduce

#EN BÜYÜK SAYIYI BULAN FONKSİYON
fonk = lambda a,b: a if(a>b) else b
print(reduce(fonk, [5,3,7,8,6,11,15,7,44,95,2,6]))

#EN BÜYÜK SAYIYI BULAN FONKSİYON
sayilar = [5,3,7,8,6,11,15,7,44,95,2,6]
def en_buyuk(self):
    b = 0
    for i in sayilar:
        a = i
        if a > b:
              b = a
    return b

print(en_buyuk(sayilar))

#FAKTORİYAL BULAN FONKSİYON
def fakt(x):
    y =1
    for i in range(x):
        if x == 1:
            return y
        else:
            y = y * x
            x -=1

print(fakt(5))

#FAKTORİYAL BULAN FONKSİYON
deger = 5
fakt2 = lambda x,y: x*y
print(reduce(fakt2, [x for x in range(1,deger+1)]))