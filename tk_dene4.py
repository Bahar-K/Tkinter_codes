from tkinter import *
from tkinter.ttk import Combobox 


pencere = Tk()

pencere.title("BAHAR")

pencere.geometry("550x350+350+50")

"""def yazdir():
	deger = acılan_kutu.get()
	print(deger)


#Acılan kutu
lis = ["Pazartesi","Salı","Çarşamba","Perşembe","Cuma"]
gun = list(range(1,24))

acılan_kutu = Combobox(pencere, values = gun, height = 16)
acılan_kutu.set("seçin")
acılan_kutu.pack()

buton = Button(pencere, text = "Yazdır",command = yazdir)
buton.pack()
"""


      #AYRI SEYLER ###################232323232323

#Spinbox(DONDURME KUTUSU)
spin = Spinbox(pencere, from_ = 1 ,to = 10)
spin.pack()

def yazdir():
	print(spin.get())

buton = Button(pencere,text ="Yazdır",command = yazdir)
buton.pack()



mainloop()