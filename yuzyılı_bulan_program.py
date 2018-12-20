# yılı girince kaçıcnı yüzyılda olduğumuzu bulan program
yil = str(input("Bir yil giriniz: "))

if len(yil) < 3:
    print("1.yüzyıl")
elif len(yil) == 3:
    if yil[1:3] == "00":
        print("{}.yüzyıl".format(yil[0]))
    else:
        print("{}.yüzyıl".format(int(yil[0])+1))
elif len(yil) == 4:
    if yil[2:4] == "00":
        print("{}.yüzyıl".format(yil[:2]))
    else:
        print("{}.yüzyıl".format(int(yil[:2]) + 1))


