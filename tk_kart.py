from tkinter import *
from random import random
import time
from tkinter import messagebox

#mainloop sonda unutma 

pencere = Tk()

pencere.title("BAHAR")

pencere.geometry("550x350+350+50")

hafiza = []
global bilinen
bilinen = 0



def cevir(a):
	if len(hafiza) == 0:
		for i in atananlar:
			if a == i[0]: #Butonun adresi
			    ilk_buton = i[2]
			    ilk_buton.config(text=i[1],
			    	state="disable")
			    hafiza.append(i) #su anda bır butona tıkladm
	else:
	    for i in atananlar:
	        	if a == i[0]:
	        		ikinci_buton=i[2]
	        		ikinci_buton.config(text=i[1],
	        			state = "disable")
	        		if i[1] == hafiza[0][1]:
	        			global bilinen
	        			bilinen = bilinen + 1
	        			hafiza.clear()
	        			if bilinen == 8:
	        				messagebox.showinfo("Hafıza Oyun","Tebrikler Hepsini Bildin :) ")
	        		else:
	        		    ikinci_buton.after(100,lambda
	        		x = i[2]:cevirici(x))	
def cevirici(ikinci_buton):
	birinci_buton = hafiza[0][2]
	birinci_buton.config(text="Eşimi bul",state="active")
	ikinci_buton.config(text="Eşimi bul",state="active")
	time.sleep(0.5)
	hafiza.clear()



#Satır sutun olusturma 
icerikler = [1,2,3,4,5,6,7,8]
icerikler = icerikler*2
atananlar = []
satirno = 0 

for satir in range(0,4):
	sütünno = 0
	for sütün in range(0,4):
		deger = len(icerikler)
		ilk = str(satirno) + str(sütünno)
		ikinci = int(random()*deger)
		butonx = Button(pencere,text = "Eşimi bul",command = lambda a = ilk: cevir(a))

		icerikler[ikinci]
		atanacak = (ilk,icerikler[ikinci],butonx)
		atananlar.append(atanacak)
		icerikler.pop(ikinci)

		butonx.grid(row=satirno,column = sütünno)

		sütünno = sütünno + 1
	satirno += 1

mainloop()