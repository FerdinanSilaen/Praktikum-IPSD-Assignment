def pencarian_biner(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return mid  # Mengembalikan indeks jika ditemukan
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Mengembalikan -1 jika tidak ditemukan

def main():
    # List hanya berisi angka genap
    list_genap = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    # Input dari pengguna
    try:
        nilai_dicari = int(input("Masukkan nilai yang ingin dicari: "))
        
        # Cek apakah nilai yang dicari ganjil
        if nilai_dicari % 2 != 0:
            print("Nilai yang dicari adalah angka ganjil. Pencarian tidak dapat dilakukan.")
            return
        
        # Melakukan pencarian biner
        indeks = pencarian_biner(list_genap, nilai_dicari)
        
        if indeks != -1:
            print(f"Nilai {nilai_dicari} ditemukan pada indeks {indeks}.")
        else:
            print(f"Nilai {nilai_dicari} tidak ditemukan dalam list.")
    
    except ValueError:
        print("Input tidak valid! Mohon masukkan angka bulat.")

# Menjalankan program
main()


