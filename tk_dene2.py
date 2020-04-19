from tkinter import *

pencere = Tk()

pencere.title("Bahar")

pencere.geometry("550x350+350+50")

#Form elemanları Checkbutton (Onay Buton)

x = IntVar()

def  kontrol():
	if x.get() == 0:
		etiket["text"] = "Seçilmedi"
	else:
	    etiket["text"] = "Seçildi"

#Direkt seçili olarak getirir 1 degeri versek  
x.set(0)

onay = Checkbutton(text= "Seç", variable = x, command = kontrol)
onay.pack()

etiket = Label()
etiket.pack()

x = StringVar()
x.set("")

def  yazdir():
	etiket["bg"] = x.get()

yazi = Label(text = "Hangi Dili öğrenmek istersin?")
yazi.pack()

kırmızı = Radiobutton(text = "Python",indicatoron = 1,variable = x,command=yazdir,value = "Red" )
kırmızı.pack()

yeşil = Radiobutton(text = "C",indicatoron = 0,variable = x,command=yazdir,value = "Green")
yeşil.pack()

mavi = Radiobutton(text = "Java",indicatoron = 0,variable = x,command=yazdir,value = "Blue")
mavi.pack()

etiket = Label()
etiket.pack()



mainloop()