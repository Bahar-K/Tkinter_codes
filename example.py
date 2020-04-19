
from tkinter import *
 
 
pencere = Tk()

pencere.title("Bahar")

pencere.geometry("260x300+500+100")
#ılk en sonra dikey boyutu yazılı+soldan sağa+ yukardan asaği

#pencere.resizable(FALSE,FALSE)
"""Bu pencereyi hareket ettirmemeyi saglar."""

pencere.minsize(100,100)
#Kücülebilecegi En kucuk deger
#pencere.maxsize(900,700)
#Buyuyebilecegi en büyük deger

#pencere.state("iconic")
#Sadece simgeye bastımızda cıkar
#pencere.state("zoomed")
#tam ekran yapar.
pencere.state("normal")
#normal olur.


#pencere.wm_attributes("-alpha", 0.9)
"""pencere saydamlastırma 0'a ne kadar
yaklasırsa o kadar saydamlasır.
"""

yazı = Label(text = "Bhr",
    fg = "green",
    bg = "yellow",
    font = ("Open Sans", "18","italic"),
    #width = 30,
    #height = 5,

    padx = 90,
    pady = 30,

    #justify = "center"
    #anchor = "s"
    )
#font parametresi icin 2.yer yazı boyutu
#font parametresi icn en son yere bunlar gelebilir. 
"""
"bold"       = Kalın yazı
"italic"     = Yana yatık yazı
"normal"     = Normal yazı
"underline"  = Altı çizgili yazı
"overstrike" = Ortası çizik yazı"""
#anchor yazı konumunu belırler


"""
justify = alacağı değerler "left","right","center"

anchor = "n" (Yukarı)
anchor = "s" (Aşağı)
anchor = "e" (Sağ)
anchor = "w" (Sol)
anchor = "ne" (Yukarı - Sağ)
anchor = "nw" (Yukarı - Sol)
anchor = "se" (Aşağı - Sağ)
anchor = "sw" (Aşağı -Sol)
anchor = "center" (Orta
"""

yazı.pack()
#pencereye label(etiket) olusturma

#Buton olusturma
def değistir():
    etiket ["text"] = "Merhaba Dünya"
    etiket ["bg"] = "green"

def kapat():
    print("HEY!! ÇIKIYORSUN...")
    quit()


etiket = Label(text = "Hello World", bg = "blue")
etiket.pack()


buton = Button(text = "Çevir",
    command = değistir)    
buton.pack()

#pasif buton
"""buton2 = Button(text ="pasif",state="disabled")
buton2.pack()"""

buton2 = Button(text ="Kapat",command = kapat)
buton2.pack()


mainloop()