def kata_terbalik(string):
    # Memisahkan string menjadi kata-kata
    kata_list = string.split()
    
    # Membalik setiap kata dan menyimpannya dalam list baru
    kata_terbalik_list = [kata[::-1] for kata in kata_list]
    
    return kata_terbalik_list

# Input dari pengguna
input_string = input("Masukkan string: ")
hasil = kata_terbalik(input_string)

# Menampilkan hasil
print(hasil)
