from tkinter import *
def veri(): # veri adlı fonksiyon açtık
   veri_brut_girdi = brut_girdi.get()                                                             # Brut girdisini getirdik
   veri_calisma_suresi_yil_girdi = calisma_suresi_yil_girdi.get()            # Calisma süresini ''yıl'' getirdik
   veri_calisma_suresi_ay_girdi = calisma_suresi_ay_girdi.get()           # calisma süresi '' ay '' getirdik
   veri_calisma_suresi_gun_girdi = calisma_suresi_gun_girdi.get()      # çalisma süresini ''gün'' getirdik
   sayı1 = int(veri_brut_girdi)     #integer haline getirdik
   sayı2 = int(veri_calisma_suresi_yil_girdi)
   sayı3 =int(veri_calisma_suresi_ay_girdi)
   sayı4 =int(veri_calisma_suresi_gun_girdi) #integer haline getirdik
   sonuc_yil = sayı1 * sayı2  #brut ile yılı çarptık
   sonuc_ay = sayı1 / 12 * sayı3 #brut ile ayı çarptık
   sonuc_gun = sayı1 / 365 * sayı4 #brut ile  günü çarptık
   toplam = sonuc_gun + sonuc_yil + sonuc_ay # çıkan sonuçları topladık (vergisiz tazminat)
   vergisiz = toplam * 0.00759 # tazminatın verigisini bulduk
   vergili = toplam - vergisiz # tazminattan vergiyi çıkardık
   kdvsiz_tazminat['text'] =  '' + str(round(vergili,2)) # round komutu ile sayıyı yuvarlardık

pencere = Tk() # pencere adlı pencereyi oluşturduk
pencere.geometry('320x210') # penceremizin boyutunu girdik
pencere.resizable(FALSE,FALSE) # pencerenin genişliği ve uzunluğu büyütülmüyor
pencere.title('Kıdem Tazminatı Hesaplama') # pencerenin başlığı
pencere.configure(background='grey') # pencerenin arka rengini gri yaptık
pencere.iconbitmap('muh.ico') # pencerenin iconunu değiştirdik

brut=Label(pencere) # label oluşturduk
brut.config(text='Brüt Maaşınızı Giriniz', bg='orange') # label üzerine yazı yazdık ve rengini belirledik
brut.pack() # label paketledik

brut_girdi = Entry(pencere) # girdi kutusu oluştukduk
brut_girdi.pack()  # girdi kutusunu paketledik

calisma_suresi_yil = Label(pencere) # label oluşturduk
calisma_suresi_yil.config(text='Kaç yıl çalıştınız?', bg='orange') # label üzerine yazı yazdık ve rengini belirledik
calisma_suresi_yil.pack()  # label paketledik

calisma_suresi_yil_girdi = Entry(pencere) # girdi kutusu oluştukduk
calisma_suresi_yil_girdi.pack() # girdi kutusunu paketledik

calisma_suresi_ay = Label(pencere)  # label oluşturduk
calisma_suresi_ay.config(text='Kaç ay çalıştınız?', bg='orange') # label üzerine yazı yazdık ve rengini belirledik
calisma_suresi_ay.pack()  # label paketledik

calisma_suresi_ay_girdi = Entry(pencere) # girdi kutusu oluştukduk
calisma_suresi_ay_girdi.pack()# girdi kutusunu paketledik

calisma_suresi_gun = Label(pencere)# label oluşturduk
calisma_suresi_gun.config(text ='Kaç gün çalıştınız?', bg='orange')# label üzerine yazı yazdık ve rengini belirledik
calisma_suresi_gun.pack()# label paketledik

calisma_suresi_gun_girdi = Entry(pencere)# girdi kutusu oluştukduk
calisma_suresi_gun_girdi.pack()# girdi kutusunu paketledik

tus = Button( text= '      Tamam      ' ,command = veri , bg='brown').pack() # buton oluşturduk ve tuşa veri fonksiyonumuzu atadık, arka rengini değiştirdik

yazi_sonuc = Label(text='  Sonuç: --Gürkan Bekdemir Tarafından Yapıldı -->', bg='black', fg='white') # label üzerine yazı yazdık, yazı ve arka renigini belirledik
yazi_sonuc.pack(side = LEFT)# label paketledik sola yerleştirdik

kdvsiz_tazminat= Label(text='                  ',bg = 'black', fg='red', )# label oluşturduk
kdvsiz_tazminat.pack(side=LEFT , )# label paketledik sola yerleştirdik

pencere.mainloop() # penceremizi paketledik
