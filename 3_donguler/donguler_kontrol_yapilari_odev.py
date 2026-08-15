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
# toplam = 0
# for i in range(11):
#     print(i)
#     toplam =toplam + i
#     print("Toplam: ",toplam)

# ============================================================
# SORU 3 (WHILE)
# Kullanıcıdan "q" yazana kadar sürekli giriş alın.
# Kullanıcı her giriş yaptığında "Girdiniz: ..." şeklinde ekrana yazdırın.
# Kullanıcı "q" yazarsa döngü bitsin ve "Çıkış yapıldı" yazsın.
# ============================================================

#######ÇÖZÜMMM
giris = ""

while giris != "q":
    giris = input("Bir şey yazın: ")
    if giris != "q":
     print(f"Girdiniz...")

print("Çıkış yapıldı...")
    
# ============================================================
# SORU 4 (NESTED)
# 1'den 20'ye kadar sayıları dolaşın.
# Eğer sayı çiftse "Çift", tekse "Tek" yazdırın.
# Ayrıca sayı 10'dan büyükse yanına "Büyük", değilse "Küçük/Eşit" yazdırın.
# Örnek çıktı: 12 -> Çift - Büyük
# ============================================================

for i in range(1,21):
   if i % 2 ==0:
      if i > 10:
       print("Çift - Büyük")
      elif i == 10:
       print("Çift - Küçük/Eşit")
      else:
        print("Çift - Küçük")
else:
      if i > 10:
       print("Tek - Büyük")
      elif i == 10:
       print("Tek - Küçük/Eşit")
      else:
       print("Tek - Küçük")
print("işlem tamamlandi")
