#filter() fonksiyonu ve diğer fonksiyonların kullanımı

filt_fonk =[2,4,5,6,8,7,9,15,19,23,21]
print(list(filter(lambda x: x%3==0, filt_fonk)))

def kısa_boler(liste):
    yeni_liste = [a for a in liste if a%3==0]
    return yeni_liste

print(kısa_boler([2,4,5,6,8,7,9,15,19,23,21]))

def uzun_boler(liste):
    yeni_liste2 = []
    for a in liste:
        if a%3==0:
            yeni_liste2.append(a)
    return yeni_liste2

print(uzun_boler([2,4,5,6,8,7,9,15,19,23,21]))

