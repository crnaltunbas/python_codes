"""
Matplotlib Nedir?
    - görselleştirme kütüphanesi
    - veriyi anlamak için görselleştiriyoruz

Matplotlib ile neler yapabiliriz?
    - line, sütun, pasta, dağılım 

Matplotlib ve Numpy/Pandas
    - Örnek veri işleme süreci
        - veri okunur (pandas)
        - veri düzenleme (pandas)
        - veri üzerinde işlemler yapılır (Numpy veya pandas)
        - veri grafikler ile gösterilir (matplotlib)

Bu bölüm ne öğreneceğiz?
    - line plot (çizgi): zaman içerisinde değişen verileri görselleştirmek için kullanırız
    - bar chart (sütun): kategorik verileri karşılaştırmak için kullanılır
    - pie chart (pasta): bir bütünün parçalarını görmek için kullanırız
    - scatter plot (dağılım): iki değişken arasında ki ilişkiyi görmek için kullanılır
    - subplots: birden fazla grafiği aynı anda gösterme         
"""

import matplotlib.pyplot as plt
print("done")


"""
line plot
"""

# çizgi grafiği oluşturma
gunler = [1, 2, 3, 4, 5]
sicaklik = [22, 24, 23, 25, 27]

# (x = gunler, y = sicaklik)
# color = renk değiştirme
# linestyle = çizgi stilini değiştirme
# marker = noktaları gösterme
plt.plot(gunler, sicaklik, color = "red", linestyle = "--", marker = "o")
plt.title("Günlere Göre Sıcaklık") # grafik başlığı
plt.xlabel("Günler") # x ekseni etiketi
plt.ylabel("Sıcaklık") # y ekseni etiketi
plt.grid(True) # alttaki kareli kısmı sağlar 
plt.show() # grafiğin ekranda görünmesini sağlar

"""
sütun grafikleri (bar charts)
"""

# sütun grafiği oluştur
isimler = ["ali", "ayse", "mehmet", "zeynep"]
notlar = [70, 85, 60, 90]

# plt.bar = sütun grafiği oluşturmak için
# (x = isimler, y = notlar) 
renkler = ["red", "blue", "green", "orange"]
plt.bar(isimler, notlar, color = renkler)
plt.title("Öğrenci Notları")
plt.xlabel("Öğrenciler")
plt.ylabel("Notlar")
plt.show()

# yatay sütun grafiği
plt.barh(isimler, notlar)
plt.show()

"""
pie chart
"""
etiketler = ["python", "java", "c++", "javascript"]
degerler = [40, 25, 20, 15]

# plt.pie = pasta grafiği
# değerler = pasta dilimlerinin büyüklüğü
# labels = her dilimin etiketi
# autopct yüzdeliklerini gösterir
# %1.1f%% = yüzdeyi 1 basamaklı ondalık ile gösterir
# explode dilimlerin ayrılmasına yardımcı olur 
ayrim = [0.1, 0, 0, 0]
renkler = ["red", "blue", "green", "orange"]
plt.pie(degerler, labels = etiketler, explode = ayrim, autopct="%1.1f%%", colors = renkler)
plt.title("Programlama Dili Kullanımı")
plt.show()

