class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_informasi(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")

    def usia_buku(self):
        from datetime import datetime
        tahun_sekarang = datetime.now().year
        return tahun_sekarang - self.tahun_terbit

# Membuat 3 objek dari class Buku
buku1 = Buku("Belajar Python", "John Doe", 2020)
buku2 = Buku("Menguasai OOP", "Jane Smith", 2018)
buku3 = Buku("Data Science untuk Pemula", "Alice Johnson", 2021)

# Menampilkan informasi dan usia masing-masing buku
for buku in [buku1, buku2, buku3]:
    buku.tampilkan_informasi()
    print(f"Usia Buku: {buku.usia_buku()} tahun\n")



