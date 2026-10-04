"""
Pandas: Veri bilimi kütüphanesi
   - Tablo şeklinde veri oluşturmak 
   - Verileri düzenlemek, filtrelemek
   - Sütun ve satır işlemleri yapmak
   - Dosyalardan veri okumak 

Pandas Numpy İlıişkisi: Pandas numpy üzerine kurulu bir pakettir

  - Numpy: Sayısal dizi sağlar 
  - Pandas : Tablo veri yapıları 

Panddas nerelerde kullanılır?

- Veri analizi
- Veri düzenleme
- Veri temizleme
- Veri işleme
- Veri dosyalarını okuma (.csv)

Pandas ile ilgili neler öğreneceğiz?
    - Series
    - dataframe
    - veri okuma ve yazma
    - veri seçme ve filtreleme
    - sütun ve satır işlemleri
    - veri sıralama ve gruplama
    - temel pandas fonksiyonları
"""

import pandas as pd

"""
Series
"""

#Seri Oluşturma

veri = pd.Series([10, 20, 30, 40])
print(veri)

"""
index value
0    10
1    20
2    30
3    40
dtype: int64

key- value(dict)
index- value(pandas series)
0: 10
1: 20
2: 30
3: 40
"""
# Series içindeki verilere erişme
veri = pd.Series([10,20,30,40])
print(veri[0]) #10
print(veri[2]) # 30

# series için özel indeks belirleme
veri = pd.Series([10, 20, 30], index = ["a", "b", "c"])
print(veri)
"""
a    10     
b    20     
c    30 
"""
print(veri["b"]) # 20

# dictionary ile series oluşturma
veri = { # anahtar-value
    "ali": 80,
    "ayse": 90,
    "mehmet": 75
}

s = pd.Series(veri)
print(s)
"""
index   value
ali       80
ayse      90
mehmet    75
"""

# series özellikleri
print(s.index) # index # Index(['ali', 'ayse', 'mehmet'], dtype='str')
print(s.values) # değerleri  # [80 90 75]
print(s.dtype) # int64

# series ile matematiksel işlemler
veri = pd.Series([10, 20, 30, 40])
sonuc = veri * 2
print(sonuc)

# series filtreleme
yas = pd.Series([10, 20, 30, 40, 50])
filtre = yas > 25 # boolean filtre
print(filtre)
"""
0    False
1    False
2     True
3     True
4     True
"""
sonuc = yas[filtre]
print(sonuc)

"""
dataframe
"""

# dataframe oluşturma
veri = {
    "isim":  ["ali", "ayse", "mehmet"],
    "yas":   [25, 30, 28],
    "sehir": ["Ankara", "İstanbul", "İzmir"] 
}

df = pd.DataFrame(veri)
print(df)
"""
sütunlar: veri kategorileri
satırlar: her bir kayıt
     isim  yas     sehir
0     ali   25    Ankara
1    ayse   30  İstanbul
2  mehmet   28     İzmir
"""

# sütun isimleri
print(df.columns) # Index(['isim', 'yas', 'sehir'], dtype='str')

# dataframe satır sayısı öğrenme
print(df.shape) # (3, 3)

# sütunlara erişim
print(df["isim"])

# birden fazla sütun seçme
print(df[["isim", "yas"]])

# yeni sütun ekleme
df["maas"] = [5000, 7000, 6000]
print(df)
"""
     isim  yas     sehir  maas
0     ali   25    Ankara  5000
1    ayse   30  İstanbul  7000
2  mehmet   28     İzmir  6000
"""

# sütun silme
df = df.drop("sehir", axis = 1)
print(df)
"""
     isim  yas  maas
0     ali   25  5000
1    ayse   30  7000
2  mehmet   28  6000
"""

# ilk satırları görüntülemek
print(df.head()) # ilk 5 satır

# son satırları görüntüleme
print(df.tail())

# dataframe hakkında bilgi alma
print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   isim    3 non-null      str
 1   yas     3 non-null      int64
 2   maas    3 non-null      int64
dtypes: int64(2), str(1)
memory usage: 204.0 bytes
"""

"""
Dosya okuma ve yazma
"""



