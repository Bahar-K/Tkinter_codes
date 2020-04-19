from tkinter import *


pencere = Tk()

pencere.title("Bahar")

pencere.geometry("260x300+500+190")

"""yazi = Entry(show = "+")
yazi.pack()
"""
giris = Label(text = "Hangi dilleri biliyorsun?")
giris.pack()

#Entry ile kullanıcı yazabılıyor.
k_giris = Entry()
k_giris.pack()

buton3 = Button(text = "Ekle",command = lambda: listekutusu2.insert(END,k_giris.get()))
buton3.pack()


#listbox olusturma
listekutusu = Listbox(selectmode = EXTENDED)
listekutusu.pack()

listekutusu.insert(END,"Python")
listekutusu.insert(END,"Java")

listekutusu2 = Listbox()
listekutusu2.pack()

buton = Button(text = "Ekle",command = lambda : listekutusu2.insert(END,listekutusu.get(ACTIVE)))
buton.pack()

buton2 = Button(text = "Sil",command = lambda :listekutusu2.delete(ACTIVE))
buton2.pack()


mainloop()