def faktorial(n):
    # Basis kasus: faktorial dari 0 adalah 1
    if n == 0:
        return 1
    else:
        # Rekursi: n! = n * (n-1)!
        return n * faktorial(n - 1)

def urutan_faktorial(n):
    # Daftar untuk menyimpan hasil faktorial
    hasil = []
    
    for i in range(1, n + 1):
        hasil.append(faktorial(i))
    
    return hasil

# Contoh penggunaan
n = 5
output = urutan_faktorial(n)
print(output)  # Output: [1, 1, 2, 6, 24]
