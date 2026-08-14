# ============================================================
# SORU 1
# Bir değişken tanımlayalım: ad = "Kaan", yas = 25, ortalama = 3.45
# Bu değişkenlerin tiplerini type() ile yazdıralım.
# ============================================================

################# ÇÖZÜM
# ad = "Kaan"
# yas = 25 
# ortalama = 3.45

# print(type(ad))
# print(type(yas))
# print(type(ortalama))

# ============================================================
# SORU 2
# Kullanıcıdan yaş bilgisini input() ile alalım.
# Bu yaşın tipini ekrana basalım ve 5 yıl ekleyip sonucu yazdıralım.
# Not: input() her zaman string döndürür, int'e çevirmeyi unutmayalım.
# ============================================================

##########ÇÖZÜM
#x = input("Yasinizi giriniz:")
# print(type(x))
# str_to_int = int(x)
# print(str_to_int + 5)

# ============================================================
# SORU 3
# Bir ürün fiyatı (float) alalım. %18 KDV hesaplayalım.
# Toplam fiyatı 2 basamak olacak şekilde yazdıralım.
# ============================================================

#########ÇÖZÜM
# urun_fiyati = float(input("Ürün fiyati giriniz: "))
# kdv = round((urun_fiyati * 18)/100, 2)
# urun_fiyati2 = urun_fiyati + kdv
# net_fiyat = int(urun_fiyati2)
# print(round(net_fiyat,2))

# ============================================================
# SORU 4
# Bir liste oluşturalım: sayilar = [10, 20, 30, 40, 50]
# - İlk elemanı yazdıralım
# - Son elemanı yazdıralım
# - 2. indexten sona kadar olan parçayı yazdıralım
# - Listeye 60 ekleyelim
# - Listedeki 20 değerini silelim
# ============================================================

#######ÇÖZÜM
# liste = [10, 20, 30, 40, 50]
# print(liste[0])
# print(liste[4])
# print(liste[2:])
# liste.append(60)
# print(liste)    
# liste.remove(20)
# print(liste)

# ============================================================
# SORU 5
# Bir tuple oluşturalım: koordinat = (12, 34)
# - Tuple içindeki değerleri unpacking ile x ve y değişkenlerine alalım
# - x ve y'yi yazdıralım
# - Tuple'ın değiştirilemediğini göstermek için (yorum satırıyla) örnek verelim
# ============================================================

#########ÇÖZÜMM
# koordinat = (12, 34)
# (x, y) = koordinat
# print(x)
# print(y)
# koordinat[0]=1
# print(koordinat)

# SORU 6
# Bir sözlük (dictionary) oluşturalım:
# ogrenci = {"isim": "Ayşe", "yas": 22, "bolum": "Yazılım"}
# - Öğrencinin ismini yazdıralım
# - "not" anahtarı ile 90 ekleyelim
# - "yas" değerini 23 yaparak güncelleyelim
# - Tüm anahtarları ve tüm değerleri yazdıralım
# ============================================================

#######ÇÖZÜM
# ogrenci = {"isim": "Ayşe", 
#             "yas": 22, 
#             "bolum": "Yazılım"}

# print(ogrenci["isim"])
# ogrenci["not"]= 90
# print(ogrenci)
# ogrenci["yas"] = 23
# print(ogrenci)
# print(ogrenci.values())
# print(ogrenci.keys())

# ============================================================
# SORU 7#
# Set oluşturalım ve tekrar edenleri temizleyelim:
# liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
# - listeyi set'e çevirip benzersiz isimleri yazdıralım
# - benzersiz isim sayısını yazdıralım
# ============================================================

######ÇÖZÜMMM
liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
unique_names= set(liste)
print(len(unique_names))

#temel değişkenler ödev


