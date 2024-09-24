# 7. Buatlah program untuk memecahkan masalah "minimum coin change". Diberikan jumlah uang dan daftar nilai koin yang tersedia (misalnya, 1, 5, 10, 25), tentukan kombinasi minimum koin yang diperlukan untuk mencapai jumlah uang tersebut. 
# Namun, program Anda harus bisa menangani koin-koin yang nilai dan jumlahnya ditentukan pengguna.

def minimum_coin_change(jumlah, koin, jumlah_koin):
    koin_tersedia = sorted(zip(koin, jumlah_koin), reverse=True, key=lambda x: x[0])
    
    kombinasi = []  
    total_koin = 0  
    for nilai_koin, stok_koin in koin_tersedia:
        jumlah_koin_dipakai = 0
        while jumlah >= nilai_koin and stok_koin > 0:
            jumlah -= nilai_koin
            stok_koin -= 1
            jumlah_koin_dipakai += 1
            total_koin += 1
        
        if jumlah_koin_dipakai > 0:
            kombinasi.append((nilai_koin, jumlah_koin_dipakai))
    
    # Jika tidak bisa mencapai jumlah uang dengan koin yang tersedia
    if jumlah > 0:
        print("Tidak mungkin mencapai jumlah yang diinginkan dengan koin yang tersedia.")
        return None
    
    return kombinasi, total_koin

# Input dari pengguna
try:
    jumlah_uang = int(input("Masukkan jumlah uang yang ingin dicapai: "))
    daftar_koin = list(map(int, input("Masukkan daftar nilai koin : ").split()))
    jumlah_per_koin = list(map(int, input("Masukkan jumlah setiap koin yang tersedia : ").split()))

    if len(daftar_koin) != len(jumlah_per_koin):
        print("Jumlah koin dan nilai koin tidak sesuai.")
    else:
        hasil = minimum_coin_change(jumlah_uang, daftar_koin, jumlah_per_koin)
        
        if hasil:
            kombinasi_koin, total_koin = hasil
            print(f"Kombinasi koin yang digunakan: {kombinasi_koin}")
            print(f"Jumlah total koin yang digunakan: {total_koin}")

except ValueError:
    print("Input tidak valid! Mohon masukkan angka bulat.")

