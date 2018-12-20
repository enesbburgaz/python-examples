from tkinter import *

pencere = Tk()

satir_no=0
for satir in range(0,4):
    sutun_no=0
    for sutun in range(0,4):
        buton = Button(pencere, text="Deneme")
        buton.grid(row=satir_no, column=sutun_no)
        print(satir_no, sutun_no)
        sutun_no +=1
    satir_no +=1

pencere.mainloop()