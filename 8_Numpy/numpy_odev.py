# SORU 1
# 1) NumPy kullanarak 1’den 20’ye kadar sayılardan oluşan bir dizi oluşturun.
# 2) Dizinin kaç eleman içerdiğini ekrana yazdırın.

#####ÇÖZÜM
import numpy as np
x = np.arange(1,20)
print(x)
print(len(x))

# SORU 2
# 1) [5, 10, 15, 20, 25] değerlerinden oluşan bir NumPy dizisi oluşturun.
# 2) Dizideki tüm elemanları 3 ile çarpın.
# 3) Sonucu ekrana yazdırın.

#####ÇÖZÜM
y = np.arange(0,26,5)
print(y)
y_new = y * 3
print(y_new)


# SORU 3
# 1) 0’dan 30’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziden sadece 10 ile 20 arasındaki elemanları slicing kullanarak seçin.

#####ÇÖZÜM
z = np.arange(0,30)
print(z)
print(z[10:20])

# SORU 4
# 1) [1,2,3] ve [4,5,6] dizilerini oluşturun.
# 2) Bu iki diziyi NumPy kullanarak birleştirin.

#####ÇÖZÜM
a = np.arange(0,4)
print(a)
b = np.arange(4,7)
print(b)
c = np.concatenate((a,b))
print(c)

# SORU 5
# 1) 1’den 12’ye kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi reshape kullanarak 3x4 boyutunda bir matrise dönüştürün.
# 3) Matrisin shape değerini yazdırın.

#####ÇÖZÜM
t = np.arange(1,13)
matrix = t.reshape(3,4)
print(t)
print(matrix)
print(f"Matris boyutu:  {matrix.shape}")


# SORU 6
# 1) Aşağıdaki matrisi oluşturun
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# 2) İkinci satırı ekrana yazdırın.
# 3) İkinci sütunu ekrana yazdırın.

#####ÇÖZÜM
t = np.arange(1,10)
matrix = t.reshape(3,3)
print(matrix)
print(matrix[1,:])
print(matrix[:,1])

# SORU 7
# 1) 3x3 boyutunda rastgele sayılardan oluşan bir matris oluşturun.
# 2) Matrisin ortalamasını hesaplayın.
# 3) Matrisin maksimum değerini yazdırın.

#####ÇÖZÜM
matrix = np.random.rand(3,3)
print(matrix)
print(np.mean(matrix))
print(np.max(matrix))


# SORU 8
# 1) [2,4,6,8] ve [1,3,5,7] dizilerini oluşturun.
# 2) Dizileri eleman bazlı çarpın.
# 3) Sonucu ekrana yazdırın.

#####ÇÖZÜM
a = np.arange(2, 10, 2)
print(a)
b = np.arange(1, 8, 2)
print(b)
carpim = np.dot(a,b)
print(carpim)
print(a*b)

# SORU 9
# 1) 1’den 9’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi 3x3 matrise dönüştürün.
# 3) Matrisin transpose’unu hesaplayın.

#####ÇÖZÜM
a = np.arange(1,10)
print(a)
matrix = a.reshape((3,3))
print(matrix)
print(matrix.T)


# SORU 10
# 1) 1 ile 50 arasında rastgele 10 tam sayı üretin.
# 2) Bu sayılardan oluşan dizinin toplamını hesaplayın.
# 3) Dizinin ortalamasını yazdırın.

#####ÇÖZÜM
c = np.random.randint(1,50,10)
print(c.sum())
print(c.mean())


