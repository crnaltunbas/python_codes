# ============================================================
# SORU 1 (IF)
# Kullanıcıdan bir sayı alın.
# Sayı pozitifse "Pozitif", negatifse "Negatif", sıfırsa "Sıfır" yazdırın.
# ============================================================

######ÇÖZÜM
# x = int(input("Lütfen bir sayı giriniz: "))
# if x > 0:
#     print("x" +" pozitif bir sayıdır")
# elif x == 0:
#     print("x" +" sıfırdır.")
# else:
#     print( "x" +" negatif bir sayıdır")

# ============================================================
# SORU 2 (FOR)
# 1'den 10'a kadar (10 dahil) sayıları yazdırın.
# Ayrıca bu sayıların toplamını hesaplayıp ekrana yazdırın.
# ============================================================

######ÇÖZÜM
toplam = 0
for i in range(11):
    print(i)
    toplam =toplam + i
    print("Toplam: ",toplam)

# ============================================================
# SORU 3 (WHILE)
# Kullanıcıdan "q" yazana kadar sürekli giriş alın.
# Kullanıcı her giriş yaptığında "Girdiniz: ..." şeklinde ekrana yazdırın.
# Kullanıcı "q" yazarsa döngü bitsin ve "Çıkış yapıldı" yazsın.
# ============================================================

#######ÇÖZÜMMM
while giris != "q":
    print("Lütfen giriş yapın...")
elif giris
# ============================================================
# SORU 4 (NESTED)
# 1'den 20'ye kadar sayıları dolaşın.
# Eğer sayı çiftse "Çift", tekse "Tek" yazdırın.
# Ayrıca sayı 10'dan büyükse yanına "Büyük", değilse "Küçük/Eşit" yazdırın.
# Örnek çıktı: 12 -> Çift - Büyük
# ============================================================

