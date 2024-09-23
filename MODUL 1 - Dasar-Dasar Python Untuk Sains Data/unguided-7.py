def minimum_coin_change(total, coins):
  """Mencari kombinasi minimum koin untuk mencapai total tertentu

  Args:
    total: Jumlah uang yang ingin ditukar
    coins: List nilai koin yang tersedia

  Returns:
    List jumlah masing-masing koin yang digunakan
  """

  coins.sort(reverse=True)  # Urutkan koin dari nilai terbesar
  result = [0] * len(coins)
  
  for i, coin in enumerate(coins):
    while total >= coin:
      total -= coin
      result[i] += 1

  return result

# Contoh penggunaan
available_coins = [25, 10, 5, 1]
amount = 67

result = minimum_coin_change(amount, available_coins)
print("Kombinasi koin minimum:", result)






def minimum_coin_change(jumlah, koin):
    # Mengurutkan koin dari yang terbesar ke yang terkecil
    koin.sort(reverse=True)
    kombinasi = []  # Menyimpan kombinasi koin yang digunakan
    total_koin = 0  # Menghitung jumlah koin yang digunakan

    for nilai_koin in koin:
        while jumlah >= nilai_koin:
            jumlah -= nilai_koin
            kombinasi.append(nilai_koin)
            total_koin += 1
    
    if jumlah > 0:
        print("Tidak mungkin mencapai jumlah yang diinginkan dengan koin yang tersedia.")
        return None
    
    return kombinasi, total_koin

# Input dari pengguna
try:
    jumlah_uang = int(input("Masukkan jumlah uang yang ingin dicapai: "))
    daftar_koin = list(map(int, input("Masukkan daftar nilai koin (pisahkan dengan spasi): ").split()))
    
    hasil = minimum_coin_change(jumlah_uang, daftar_koin)
    
    if hasil:
        kombinasi_koin, total_koin = hasil
        print(f"Kombinasi koin yang digunakan: {kombinasi_koin}")
        print(f"Jumlah koin yang digunakan: {total_koin}")

except ValueError:
    print("Input tidak valid! Mohon masukkan angka bulat.")
