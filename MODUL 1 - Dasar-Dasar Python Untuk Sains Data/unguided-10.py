# 10. Buatlah program yang mengimplementasikan algoritma pencarian biner, namun dengan modifikasi: algoritma harus bisa mencari nilai di list yang hanya berisi angka genap, dan jika nilai yang dicari adalah angka ganjil, program harus menampilkan pesan bahwa nilai tersebut tidak bisa ditemukan.

def pencarian_biner(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return mid  
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1  

def main():
    list_angka = [4, 7, 16, 25, 26, 31, 56, 67, 69, 72, 89, 99]

    # Input dari pengguna
    try:
        nilai_dicari = int(input("Masukkan nilai yang ingin dicari: "))
        
        # Cek apakah nilai yang dicari ganjil
        if nilai_dicari % 2 != 0:
            print("Nilai yang dicari adalah angka ganjil. Pencarian tidak dapat dilakukan.")
            return
        
        # Melakukan pencarian biner
        indeks = pencarian_biner(list_angka, nilai_dicari)
        
        if indeks != -1:
            print(f"Nilai {nilai_dicari} ditemukan pada indeks {indeks}.")
        else:
            print(f"Nilai {nilai_dicari} tidak ditemukan dalam list.")
    
    except ValueError:
        print("Input tidak valid! Mohon masukkan angka bulat.")

# Menjalankan program
main()


