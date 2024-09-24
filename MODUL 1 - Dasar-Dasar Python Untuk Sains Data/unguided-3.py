# 3. Buat sebuah program untuk mensimulasikan transaksi ATM. Program harus:
#a. Meminta pengguna memasukkan PIN (dibatasi 3 kali percobaan).
#b. Setelah PIN benar, meminta jumlah penarikan.
#c. Jika saldo kurang dari jumlah yang ditarik, munculkan pesan kesalahan.
#d. Jika penarikan berhasil, tampilkan saldo akhir.


def transaksi_atm():
  pin_benar = "ferdi26"
  saldo = 1000000

  for i in range(3):
    pin = input("Masukkan PIN: ")
    if pin == pin_benar:
      break
    else:
      print("PIN salah. Sisa percobaan:", 2 - i)
  else:
    print("PIN salah terlalu banyak. Transaksi dibatalkan.")
    return

  while True:
    try:
      jumlah_tarik = int(input("Masukkan jumlah yang ingin ditarik: "))
      if jumlah_tarik > saldo:
        raise ValueError("Saldo tidak mencukupi.")
      else:
        saldo -= jumlah_tarik
        print("Penarikan berhasil. Saldo Anda sekarang:", saldo)
        break
    except ValueError as e:
      print(e)

# Memanggil fungsi
transaksi_atm()