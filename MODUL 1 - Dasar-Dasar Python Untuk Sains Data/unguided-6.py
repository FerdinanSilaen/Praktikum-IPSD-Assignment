# 6. Buat fungsi rekursif yang menerima input bilangan bulat `n` dan menghasilkan urutan bilangan seperti berikut ini:
#Input: n = 4
#Output: 1, 1, 2, 6, 24

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def urutan_faktorial(n):
    if n == 1:
        return [1, 1]
    else:
        hasil = urutan_faktorial(n - 1)
        hasil.append(faktorial(n))
        return hasil


n = 4
result = urutan_faktorial(n)
print(result) 
