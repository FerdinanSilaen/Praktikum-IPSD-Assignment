def transaksi_atm():
  pin_benar = "1234"  # Ganti dengan PIN yang sebenarnya
  saldo = 1000000

  for i in range(3):
    pin = input("Masukkan PIN: ")
    if pin == pin_benar:
      break
    else:
      print("PIN salah. Sisa percobaan:", 2 - i)
  else:
    print("PIN salah terlalu banyak kali. Transaksi dibatalkan.")
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



def atm_simulator():
    # Inisialisasi saldo dan PIN
    saldo = 100000  # Saldo awal
    pin = "1234"  # PIN yang benar
    max_attempts = 3  # Maksimal percobaan PIN
    attempts = 0  # Hitung percobaan

    # Meminta pengguna memasukkan PIN
    while attempts < max_attempts:
        user_pin = input("Masukkan PIN Anda: ")
        
        if user_pin == pin:
            print("PIN benar! Anda dapat melakukan penarikan.")
            break
        else:
            attempts += 1
            print(f"PIN salah! Anda memiliki {max_attempts - attempts} percobaan tersisa.")
    
    # Jika percobaan PIN habis
    if attempts == max_attempts:
        print("Akun Anda diblokir setelah 3 percobaan gagal.")
        return

    # Meminta jumlah penarikan
    try:
        jumlah_tarik = float(input("Masukkan jumlah penarikan: "))
        
        if jumlah_tarik > saldo:
            raise ValueError("Saldo tidak cukup untuk melakukan penarikan.")
        
        # Memproses penarikan
        saldo -= jumlah_tarik
        print(f"Penarikan berhasil! Saldo akhir Anda adalah: {saldo}")
    
    except ValueError as e:
        print(f"Kesalahan: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Menjalankan simulator ATM
atm_simulator()
