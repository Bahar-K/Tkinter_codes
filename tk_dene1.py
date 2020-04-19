from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
#mainloop sonda unutma 

pencere = Tk()

pencere.title("BAHAR")

pencere.geometry("550x350+350+50")

def about():
	print("OUR COMPANY İS GOOD LİKE U")

def kaydet():
	filedialog.asksaveasfile(initialdir = "/",
		title = "Dosya Kaydet",
		filetype = (("*jpg Files","*.jpg"),("All Files","*.*")))

#Form elemanları messagebox Dialog
 
#messagebox.showinfo("Bilgi","Bilgi Ekranı")
#messagebox.showwarning("Uyarı","Uyarı Ekranı")
#messagebox.showerror("Hata","Hata Göster")
#soru = messagebox.askquestion("Soru","Soru Ekranı")
#ok_iptal = messagebox.askokcancel("Tamam","Tamam mı Devam mı")
#evet_hayır = messagebox.askyesno("Cıkmak","Cıkmak istermısın ?")
#tekrar_iptal = messagebox.askretrycancel("tekrar iptal","Tekrar denemek ister misin? ")

#Ana peneceremızın adı neyse yaz yanı Tk ya esıtledıgımızın adını
menubar = Menu(pencere)


dosya_menu = Menu(menubar, tearoff = 0)
#İLK Alt baslıkları olusturuyoruz 
dosya_menu.add_command(label = "Yeni")
dosya_menu.add_command(label = "Aç")
dosya_menu.add_command(label = "Kaydet",command = kaydet)

#Ana menü 
menubar.add_cascade(label = "Dosya", menu = dosya_menu)

#AYRI YER ####
duzen_menu = Menu(menubar, tearoff = 0)
duzen_menu.add_command(label = "Gei Al")
duzen_menu.add_separator() #Araya cızgı eklıyor.
duzen_menu.add_command(label = "Kes")
duzen_menu.add_command(label = "Kopyala")

menubar.add_cascade(label = "Düzen", menu = duzen_menu)

######
help_menu = Menu(menubar,tearoff = 0)

help_menu.add_command(label = "Documentation")
help_menu.add_command(label = "Twitter")
help_menu.add_separator()
help_menu.add_command(label = "About this app", command = about)
help_menu.add_separator()
help_menu.add_command(label = "Exit",command = quit)


menubar.add_cascade(label = "Help", menu = help_menu)



pencere.config(menu = menubar)



mainloop()