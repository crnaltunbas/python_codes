import matplotlib.pyplot as plt


# ÖRNEK VERİ SETİ
# Aşağıdaki veri seti tüm sorular için kullanılacaktır.

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"]
satislar = [120, 150, 170, 160, 200, 220]
karlar = [20, 35, 40, 30, 50, 60]
reklam = [5, 8, 10, 7, 12, 15]


# SORU 1
# Aylar ve satışlar verisini kullanarak basit bir çizgi grafiği oluşturun.

plt.plot(aylar, satislar, color ="red", linestyle = "-")
plt.xlabel("Aylar")
plt.title("Soru 1 Grafiği")
plt.ylabel("Satışlar")
plt.show()

# SORU 2
# Aylar ve kârlar verisini kullanarak çizgi grafiği oluşturun.
# Çizgi rengi kırmızı olsun.

plt.plot(aylar, karlar, color ="red", linestyle= "-", marker ="*")
plt.xlabel("Aylar")
plt.ylabel("Karlar")
plt.title("Soru 2 Grafiği")
plt.show()

# SORU 3
# Aylar ve satışlar verisini kullanarak marker'lı bir çizgi grafiği oluşturun.

plt.plot(aylar, satislar, color ="orange", linestyle = "-" , marker = ".")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.title("Soru 3 Grafiği")
plt.show()

# SORU 4
# Aylar ve satışlar verisini kullanarak sütun grafiği oluşturun.

plt.bar(aylar, satislar)
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.title("Soru 4 Grafiği")
plt.show()

# SORU 5
# Aylar ve reklam verisini kullanarak yeşil renkli bir sütun grafiği oluşturun.

plt.bar(aylar, satislar, color ="green")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.title("Soru 5 Grafiği")
plt.show()

# SORU 6
# Satışlar verisini kullanarak pasta grafiği oluşturun.
# Ay isimlerini etiket olarak gösterin ve yüzdeleri ekrana yazdırın.

plt.pie(satislar, labels=aylar, explode=[0, 0, 0, 0, 0, 0.1], autopct='%1.1f%%')
plt.title("Soru 6 Grafiği ")
plt.show()

# SORU 7
# Reklam ve satışlar verisini kullanarak scatter plot oluşturun.

plt.scatter(reklam, satislar, s=75)
plt.xlabel("Reklam")
plt.ylabel("Satışlar")
plt.title("Soru 7 Grafiği")
plt.show()

# SORU 8
# Reklam ve kâr verisini kullanarak kırmızı renkli ve büyük noktalı scatter plot oluşturun.

plt.scatter(reklam, karlar,color= "red", s=125)
plt.xlabel("Reklam")
plt.ylabel("Karlar")
plt.title("Soru 8 Grafiği")
plt.show()

# SORU 9
# Aynı figür içinde 1 satır 2 sütun olacak şekilde iki grafik oluşturun.
# Solda satışlar için line plot, sağda kârlar için bar chart gösterin.

plt.subplot(1,2,1)
plt.plot(satislar, aylar, color="red")
plt.title("Soru 9.1 Grafiği")

plt.subplot(1,2,2)
plt.bar(karlar, aylar,color="blue")
plt.title("Soru 9.2 Grafiği")
plt.show()

# SORU 10
# 2 satır 2 sütun olacak şekilde 4 farklı grafik oluşturun.
# 1. grafik: satışlar line plot
# 2. grafik: kârlar bar chart
# 3. grafik: reklam-satış scatter plot
# 4. grafik: satışlar pie chart

plt.subplot(2,2,1)
plt.plot(satislar, aylar, color = "red")
plt.title("Soru 10.1 Grafiği")

plt.subplot(2,2,2)
plt.bar(karlar,aylar, color="blue")
plt.title("Soru 10.2 Grafiği")

plt.subplot(2,2,3)
plt.scatter(reklam,satislar, s=25,color= "yellow")
plt.title("Soru 10.3 Grafiği")

plt.subplot(2,2,4)
plt.pie(satislar, labels= aylar, explode=[0, 0, 0, 0, 0, 0.1],autopct= '%1.1f%%')
plt.title("Soru 10.4 Grafiği")

plt.show()
