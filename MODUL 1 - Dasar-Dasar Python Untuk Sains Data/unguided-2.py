# 2. Buat variabel untuk menyimpan nilai luas dan keliling lingkaran, hitung hasilnya.

def ambil_indeks_ganjil(list1, list2):
    hasil = [list1[i] for i in range(1, len(list1), 2)] + [list2[i] for i in range(1, len(list2), 2)]
    hasil.sort(reverse=True)
    return hasil

list_angka1 = [1, 2, 3, 4, 8]
list_angka2 = [11, 13, 14, 17, 23, 37]
hasil = ambil_indeks_ganjil(list_angka1, list_angka2)
print(hasil) 

