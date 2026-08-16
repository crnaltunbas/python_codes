"""
Hata yönetimi: 
    - hata (error) ve ististna (exception) 
    - en sık karşılaşılan hata tipleri

Neden önemli:
    - hata yönetimi programın çökmeden kontrollü bir şekilde çalışmasını sağlar

hata yönetimi = can dostumuz

yapay zeka da nerelerde kullanılır?
    - veri hazırlama
    - dosya okuma
    - model eğitim döngüsü
    - rag sistemleri
"""

# yazım hatası (syntax error)
if 5 > 3: # SyntaxError: expected ':'
    print("ok") # NameError: name 'ok' is not defined

# name error (tanımsız değişken)
# print(x) # NameError: name 'x' is not defined

# type error (tip uyusmazlığı)
# print("10" + 5) # TypeError: can only concatenate str (not "int") to str

# value error (değer uygun değil)
# int("kaan") # ValueError: invalid literal for int() with base 10: 'kaan'

# zero division error (sifra bölme hatası)
# print(10/0) # ZeroDivisionError: division by zero

# indeks hatası 
liste = [1, 2, 3, 4]
# print(liste[10]) # IndexError: list index out of range

# key error (sözlükte anahtar hatası)
ogrenci = {"isim": "kaan"}
# print(ogrenci["yas"]) # KeyError: 'yas'

# file not found hatası
# with open("kaan.txt", "r") as f:
#     print(f.read()) # FileNotFoundError: [Errno 2] No such file or directory: 'kaan.txt'

# attribute hatasi (yanlış metot özellik hatası)
sayi = 10
# sayi.append(5)  # AttributeError: 'int' object has no attribute 'append'

