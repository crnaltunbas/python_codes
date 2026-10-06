"""
Class Nedir?    
    - bir nesnenin (object) nasıl olacağını tanımlayan bir şablondur.
    - class bir taslak yada plan gibidir
    - öğrenci:
        - isim, yaş, bmlüm 
        - ders çalışmak, sınava girmek 

Class tanımlama: Ogrenci > class ismi
class Ogrenci:
    pass
    
Class neden kullanırız?
    - kodun daha düzenli olması için
    - kod tekrarını azaltır
    - büyük projelerde yönetimi kolaylaştırır
    - scikit learn -> en önemli machine learning kütüphanesi -> LinearRegression() class tanımlamış olur.

Neler Öğreneceğiz?
    - __init__ metodu (initializer): nesne oluşturulduğunda otomatik olarak çalışan özel bir metottur. (kurucu metod)
    - attribute ve method
    - object oluşturma
    - Mini proje
"""

"""
Ogrenci class
    - isim
    - yaş
"""
class Ogrenci:

    def __init__(self, isim, yas): # self = oluşturulan nesneyi temsil eder, isim ve yaş başlangıç parametrelerimiz
        print(f"Yeni bir öğrenci oluşturuluyor: isim: {isim}, yaş: {yas}")

# nesne (object) oluşturma
ogrenci1 = Ogrenci("Ali", 21)
