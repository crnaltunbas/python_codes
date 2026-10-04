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
## dosya okuma için openpyxl paketi kurulmalı 

# csv (comma separated values) dosyası okuma
df = pd.read_csv("9_pandas/veri.csv")
print(df)

# excel okuma
df = pd.read_excel("9_pandas/veri_excel.xlsx")
print(df)
"""
     isim  yas  not
0    kaan   35   95
1     can   25   90
2  yılmaz   30   85
"""

# csv dosyası yazma
veri = {
    "isim": ["ali", "ayse", "mehmet"],
    "yas": [25, 30, 35]
}

df = pd.DataFrame(veri)
# df.to_csv("veri_output.csv", index=False)

# excel dosyası yazma
df.to_excel("veri_output.xlsx", index=False)

"""
Veri seçme ve filtreleme
"""

veri = {
    "isim": ["ali", "ayse", "mehmet", "zeynep", "ahmet"],
    "yas":  [25, 30, 28, 35, 22],
    "sehir": ["Ankara", "İstanbul", "İzmir", "Ankara", "Bursa"],
    "maas": [5000, 7000, 6000, 8000, 4500] 
}
df = pd.DataFrame(veri)
print(df)

# sütun seçme
print(df["isim"])

# birden fazla sütun seçme
print(df[["isim", "maas"]])

# satır seçme: iloc
print(df.iloc[0])
"""
isim        ali
yas          25
sehir    Ankara
maas       5000
"""

# birden fazla satır
print(df.iloc[0:3])

# satır seçme: loc
# indekslere göre seçmeyi sağlar yani etiketine göre 

print(df.loc[2])
"""
isim     mehmet
yas          28
sehir     İzmir
maas       6000
"""

# belirli bir satır ve belirli bir sütun
print(df.loc[:, ["isim", "maas"]])

print(df.loc[:2, ["isim", "maas"]]) # 2 dahil olur 

# koşullu filtreleme
filtre = df["yas"] > 30
print(filtre)
"""
0    False
1    False
2    False
3     True
4    False
"""
sonuc = df[filtre]
print(sonuc)

print(df[df["yas"] > 30])

# birden fazla koşul varsa
# şehir ankara ve maas 6000 den büyük olan insaları getir
sonuc = df[(df["sehir"] == "Ankara") & (df["maas"] > 6000)]
print(sonuc)

# belirli bir değeri içeren satılar
print(df[df["sehir"] == "Ankara"])

# sadece belirli sütunları gösterme
# yaşı 25 den büyük olan verinin sadece isim ve maaşını göster
print(df[df["yas"] > 25][["isim", "maas"]])


"""
Sütun ve satır işlemleri
"""

# dataframe oluştur
veri = {
    "isim": ["ali", "ayse", "mehmet"],
    "yas": [25, 30, 28],
    "maas": [5000, 7000, 6000]
}

df = pd.DataFrame(veri)
print(df)

# yeni bir sütun ekleme
df["sehir"] = ["Ankara", "İstanbul", "İzmir"]
print(df)

# hesaplama ile sütun oluşturma
df["yillik_maas"] = df["maas"] * 12 
print(df)

# sütun silme
df = df.drop("maas", axis = 1)
print(df)

# sütun isim değiştirme
df = df.rename(columns={"yillik_maas": "yillikMaas"})
print(df)

# yeni satır eklemek
df.loc[3] = ["Zeynep", 32, "Ankara", 80000]
print(df)

# satır silme
df = df.drop(0)
print(df)

# index değerlerini yeniden düzenleme
df = df.reset_index(drop = True)
print(df)

"""
Veri sıralama ve gruplama
"""

# örnek data frame oluştur
veri = {
    "isim": ["ali", "ayse", "mehmet", "zeynep", "ahmet"],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500]
}

df = pd.DataFrame(veri)
print(df)
"""
     isim     sehir  maas
0     ali    Ankara  5000
1    ayse  İstanbul  7000
2  mehmet    Ankara  6000
3  zeynep     İzmir  8000
4   ahmet  İstanbul  4500
"""
# veri sıralama
df_sirali = df.sort_values("maas")
print(df_sirali)

"""
     isim     sehir  maas
4   ahmet  İstanbul  4500
0     ali    Ankara  5000
2  mehmet    Ankara  6000
1    ayse  İstanbul  7000
3  zeynep     İzmir  8000
"""

# azalan sıralama
df_sirali = df.sort_values("maas", ascending=False)
print(df_sirali)
"""
     isim     sehir  maas
3  zeynep     İzmir  8000
1    ayse  İstanbul  7000
2  mehmet    Ankara  6000
0     ali    Ankara  5000
4   ahmet  İstanbul  4500
"""

# birden fazla sütuna göre sıralama
df_sirali = df.sort_values(["sehir", "maas"])
print(df_sirali)
"""
     isim     sehir  maas
0     ali    Ankara  5000
2  mehmet    Ankara  6000
4   ahmet  İstanbul  4500
1    ayse  İstanbul  7000
3  zeynep     İzmir  8000
"""

# veri gruplama: groupby
# şehir bazında gruplama
gruplar = df.groupby("sehir")
print(gruplar) # <pandas.api.typing.DataFrameGroupBy object at 0x000001DBF8751160>

# grupların ortalama maaşı
sonuc = df.groupby("sehir")["maas"].mean() # şehir bazında ortalama maaş hesaplama
print(sonuc)
"""
Ankara      5500.0
İstanbul    5750.0
İzmir       8000.0
"""

# grupların toplam maaşı
sonuc = df.groupby("sehir")["maas"].sum()
print(sonuc)
"""
sehir
Ankara      11000
İstanbul    11500
İzmir        8000
"""

# grupların kaç kişi olduğunu bulalım
sonuc = df.groupby("sehir")["isim"].count()
print(sonuc)
"""
sehir
Ankara      2
İstanbul    2
İzmir       1
"""

# birden fazla işlem yapma
sonuc = df.groupby("sehir")["maas"].agg(["mean", "max", "min"])
print(sonuc)
"""
            mean   max   min
sehir
Ankara    5500.0  6000  5000
İstanbul  5750.0  7000  4500
İzmir     8000.0  8000  8000
"""
