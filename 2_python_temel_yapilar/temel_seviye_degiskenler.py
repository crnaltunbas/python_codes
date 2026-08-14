"""

Değişken Kavramı : Veriyi saklamak için kullandığımız isimlendirilmiş bir alandır.
   -değişken = bilgiyi tuttuğumuz kutu
   -değişkenleri isimlendirme kuralları:
   -rakamlarla başlamaz
   -boşluk içermez
   -özel karakter içermez
   -büyük harf küçük harf ile duyarlıdır.

 - Integer: tam sayıları temsil eden değişken tipidir.
 - Float:Ondalıklı sayıları temsil eder 
 - String: Metinsel Verileri temsil eder 
 - Veri Tipi Kontrolü ve Tip Dönüşümleri:Bir değişkeni hangi veri tipinde olduğunu öğrenmek ve veri tipleri arasında dönüşüm yapmak
 - Lists: Birden fazla veriyi tek  bir değişken içerisinde saklamamızı sağlar.
   -indeksleme ve slicing
   -list metotları
 - Tuple: Birden fazla veriyi saklayan bir veri yapısıdır. Değiştirilemez(immutable)
 - Dictionary(Sözlük): Veriler anahtar - değer (key-value) şeklinde saklar.
 - Set: Benzersiz yani unique elemanlardan oluşan bir veri yapsıdır yani aynı elemandan birden fazla olamaz 
 - Veri Yapıları arasındaki farklar

"""
# Integer
# yas = 35
# ogrenci_sayisi=55000
# sicaklik= -15
# print(yas)

# Hesaplama
 
# a = 10
# b = 5

# toplama = a + b
# print(toplama)

# carpma = a * b
# print(carpma)

# cikarma = a - b
# print(cikarma)

# bolme = a/b
# print(bolme)

#gerçek hayat örneği: Ürün sayisi ve her bir ürünün birim fiyatı  amaç:toplam ürün fiyati

# urun_sayisi = 8 # 8 adet ürün var 
# birim_fiyat = 10 # birim fiyat 10 tl

# toplam = urun_sayisi * birim_fiyat
# print(toplam)

# # zam uygulaması 

# birim_fiyat = 10
# yuzde=int(input("Yüzde yazınız: "))
# print(yuzde)
# zamli_fiyat = birim_fiyat + birim_fiyat*yuzde/100
# print(zamli_fiyat)

# ctrl+ö comment kısayolu 
#Float 

# pi=3.14
# #pi=3,14 bu yanlış

# sicaklik=35.5
# urun_fiyati=99.99

# print(sicaklik)

#matematiksel işlemler 
# a = 3.5
# b = 2.0

# print(a+b)

# print(a/b)

# #ondalık hassasiyeti
# print(0.1+0.2) #0.3 ->0.3000000004

#yuvarlama (round)

# sonuc = 0.1 + 0.2
# print(sonuc)

# sonuc_yuvarlanmis = round(sonuc,2)
# print(sonuc_yuvarlanmis)

# #proje:gelen fiyat üzerinden kdv (%20) hesapla
# fiyat = float(input("Fiyat girin: "))
# print(fiyat)
# kdvli_fiyat =fiyat + 20*fiyat/100
# print(kdvli_fiyat)

# #String
# isim = "Ceren"
# sirket = 'ucanble'

# bilgi = "Cerenin çalıştığı firmanın ismi ucable"
# print(bilgi)

# #String birleştirme (concatenation)
# isim = "Ceren"
# sirket = 'ucanble'
# bilgi2 = isim + " çalıştığı firmanın ismi " + sirket 

# # Sayı ve string birleştirme 
# yas = 24 #int
# int_to_str= str(yas) # 35 -> "35"
# isim = 'Ceren' #String 
# sonuc = isim + " hocanın yaşı: " + int_to_str # ceren hocanın yaşı: 24
# print(sonuc)

# kurulum_tarihi = 2023
# print("Ucanble teknoloji " + str(kurulum_tarihi) + " yılında kurulmuştur")
# print(f"Ucanble teknoloji {kurulum_tarihi} yılında kurulmuştur. ")# f string 

# accurancy = 95
# print(f"Karar ağacı accurancy: {accurancy}%")

# #String indexleme 
# kelime = "python" # string = karakter dizisi 
# print(kelime[0])
# # print(kelime[3])

# # #String Metodları 
# # metin = "Python"
# # metin_kucuk_harf = metin.lower()
# # print(metin_kucuk_harf)

# # #Uzunluk Bulma
# # metin = "python"
# # metin_uzunlugu = len(metin)
# # print(metin_uzunlugu)

# # #Yer değiştirme
# # metin = "python"
# # print(metin.replace("o","O"))

# # # Veri Tipi kontrolü
# # x=10
# # print(type(x))#<class 'int'>

# # x="100"
# # print(type(x))#<class 'str'>
# # #tip dönüşümleri (casting)

# # x="25"
# # print(type(int(x)))#<class 'int'>
# # print(type(float(x))) #<class 'float'>

# # x = 35
# # print(type(str(x))) #<class 'str'>

# # sayi =int(input("Bir sayı girin: ")) #input fonksiyonu çıktısı ne olabilir int? str?
# # print(sayi) #45 int? str?
# # print(type(sayi))#<class 'str'>

# # print(int('abc'))#ValueError: invalid literal for int() with base 10: 'abc'

# #Listeler 
# #Liste tanımlaması köşeli parantez[] ile gerçekleşir
# sayilar = [1,2,3,4,5,6] # integer listesi 
# isimler = ["Kaan", "Ceren", "Bubilet"] #String Listesi 
# karisik = ["Kaan", "Ceren", "Bubilet", "Altunbas", 24, 2024.0] # Farklı veri tiplerini aynı anda tutabilir 
# print(karisik) 

# # Liste indeksleme : listelerde indeks 0'dan başlar 

# meyveler = ["elma","muz","kivi"]
# print(meyveler[0])#elma
# print(meyveler[2])#kivi
# print(meyveler[-1])#kivi

# #Liste uzunluğu 
# print(len(meyveler))#3

# #Liste Slicing 

# sayilar = [10,20,30,40,50,60]
# print(sayilar[1:4]) #20, 30, 40 [a:b] a dahil, b dahil değil
# print(sayilar[0:3]) #ilk 3 eleman 10, 20, 30
# print(sayilar[:3])#ilk 3 eleman 10, 20, 30
# print(sayilar[2:])#30 dan sonrası [30,40,50,60]


# #Listeye eleman eklemek 
# sayilar=[1,2,3]
# sayilar.append(4)
# print(sayilar)# [1,2,3,4]

# sayilar.insert(1,100)
# print(sayilar) #[1,100,2,3,4]

# sayilar.remove(100) # sayilar silme 
# print(sayilar)

# sayilar.pop() #en son indekste bulunan değer çıkartılır
# print(sayilar)

# sayilar.pop(0)#belirli bir indeks silme 
# print(sayilar)

# sayilar[0] = 999 # belirli bir indeksdeki değeri başka bir değer ile değiştirir
# print(sayilar) #[999,3]

# #Tuple ->()
# koordinat = (10,20)
# renkler = ("kirmizi", "mavi", "yesil")

# #Liste vs. Tuple

# liste=[1,2,3]
# liste[0]=99 #çalışır
# print(liste) #[99,2,3]

# tup = (1,2,3)
# tup[0]=99
# print(tup)#TypeError: 'tuple' object does not support item assignment

# #indeksleme 
# t=(10, 20, 30)
# print(t[1])#20
# print(t[-1])#30

# # slicing 
# # t = (10, 20, 30, 40)
# # print(t[1:3]) #(20,30)

# #tek elemanlı tuple 
# x= (5) # x =5
# print(type(x)) # tuple? int? cevap <class 'int'>

# x = (5,)
# print(type(x))#<class 'tuple'>

# #tuple unpacking
# koordinat = (10, 20)
# x, y = koordinat
# print(x) #10
# print(y) #20

# #tuple metodları

# t = (10, 20, 30, 40)
# print(t.count(20)) #2
# print(t.index(30)) #2

#dictionary(sözlük)

# ogrenci = {
#     "isim": "ali",
#     "yas": 25,
#     "bolum":"matematik"
# }
# print(ogrenci)

# # dictionary ye erişim
# print(ogrenci["isim"]) # ali
# print(ogrenci["yas"])

# # dictionary yeni değer ekleme
# ogrenci["not"] = 85
# print(ogrenci) # {'isim': 'ali', 'yas': 25, 'bolum': 'bilgisayar', 'not': 85}

# # dictionary değer güncelleme
# ogrenci["yas"] = 26
# print(ogrenci) # {'isim': 'ali', 'yas': 26, 'bolum': 'bilgisayar', 'not': 85}

# # dictionary eleman silme
# del ogrenci["bolum"]
# print(ogrenci) # {'isim': 'ali', 'yas': 26, 'not': 85}

# # anahtarları ve değerleri al
# print(ogrenci.keys()) # anahtarlar
# print(ogrenci.values()) # değerler
# print(ogrenci.items()) # anahtar - değer 

# """
# dict_keys(['isim', 'yas', 'not'])
# dict_values(['ali', 26, 85])
# dict_items([('isim', 'ali'), ('yas', 26), ('not', 85)])
# """


# set
sayilar = {1, 2, 3, 4}
print(sayilar) # {1, 2, 3, 4}

# set tekrar eden elemanlar
sayilar = {1, 2, 2, 3, 3, 3}
print(sayilar) # {1, 2, 3}

# set özellikleri: setler sırasızdır yani indeksi yoktur
# print(sayilar[2]) # TypeError: 'set' object is not subscriptable

# listeyi set e çevirme
liste = [1, 2, 2, 3, 4, 4]
benzersiz = set(liste)
print(benzersiz) # {1, 2, 3, 4}

# set eleman ekleme
sayilar.add(5)
print(sayilar) # {1, 2, 3, 5}

# set eleman silme
sayilar.remove(2)
print(sayilar) # {1, 3, 5}

# set işlemleri
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b)) # birleşim {1, 2, 3, 4, 5}
print(a.intersection(b)) # kesişim {3}
print(a.difference(b)) # fark {1, 2}

"""
VERİ YAPILARI ARASINDAKİ FARKLAR

liste:
    - sıralıdır, değiştirilebilir, tekrar eden elemanlara izin verir
    - liste = [1, 2, 3]
    - kullanım: eleman sırası önemliyse, veri güncellenecekse
    - numpy array in temelini oluşturmaktadır

Tuple:
    - sıralıdır, değiştirilemez, tekrar eden elemanlara izin verir
    - tuple = (1, 2, 3, 4)    
    - kullanım: veri sabit kalacaksa, güvenli yapı gerekiyorsa

dictionary:
    - anahtar-değer (key-value pair)
    - anahtarlar benzersizdir
    - değerler tekrar edebilir
    - değiştirilebilir
    - ogrenci = {"isim":"kaan", "yas": 35}
    - anlamlı veri saklamak, etiketli veri tutmak
    - pandas dataframe temelini oluşturur

Set:
    - sırasızdır, tekrar eden elemanları kabul etmez, değiştirilebilir
    - set = {1, 2, 3, 4}
    - kullanım: tekrar eden değerleri temizlemek için, küme işlemleri yapmak için
"""

#temel değişkenler
