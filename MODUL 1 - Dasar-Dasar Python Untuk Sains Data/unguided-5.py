import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    percobaan = 5

    print("Selamat datang di permainan tebak angka!")
    print("Tebak angka antara 1 sampai 100.")

    while percobaan > 0:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
            if tebakan == angka_rahasia:
                print("Selamat, Anda berhasil menebak!")
                return
            elif tebakan < angka_rahasia:
                print("Terlalu rendah.")
            else:
                print("Terlalu tinggi.")
            percobaan -= 1
        except ValueError:
            print("Masukkan angka yang valid.")

    print("Anda kehabisan percobaan. Angka rahasianya adalah:", angka_rahasia)

# Memulai permainan
tebak_angka()