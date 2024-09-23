def ambil_indeks_ganjil(list1, list2):
    # Mengambil elemen dengan indeks ganjil dari kedua list menggunakan list comprehension
    hasil = [list1[i] for i in range(1, len(list1), 2)] + [list2[i] for i in range(1, len(list2), 2)]
    
    # Mengurutkan hasil secara menurun
    hasil.sort(reverse=True)
    
    return hasil

# Contoh penggunaan
list_angka1 = [1, 3, 5, 7, 9]
list_angka2 = [2, 4, 6, 8, 10]
hasil = ambil_indeks_ganjil(list_angka1, list_angka2)
print(hasil) 