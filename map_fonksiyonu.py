
sayilar = [2,4,8,16,32]
print(list(map(lambda x: x*2, sayilar)))

def karesi(gelen):
    liste = []
    for i in gelen:
        liste.append(i*2)
    return liste

print(karesi([64,128,256,512]))

a = [2,4,8,16,32]
b = [64,128,256,512,1024]
print(list(map(lambda x,y: x*y, a,b)))

bilgiler = [("enes",90),("ahmet",40),("hasan",75)]
durum = lambda i: (i[0], "geçti" if i[1]>70 else "kaldı")
print(list(map(durum,bilgiler)))