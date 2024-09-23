



def binary_search_even(arr, x):
  """Pencarian biner untuk angka genap dalam list terurut

  Args:
    arr: List yang sudah terurut berisi angka genap
    x: Angka yang dicari

  Returns:
    Indeks jika ditemukan, -1 jika tidak ditemukan
  """

  # Cek jika angka yang dicari ganjil
  if x % 2 != 0:
    return -1

  low = 0
  high = len(arr) - 1
  mid = 0

  while low <= high:
    mid = (high + low) // 2

    # Jika x berada di tengah
    if arr[mid] == x:
      return mid

    # Jika x lebih besar dari mid
    elif arr[mid] < x:
      low = mid + 1

    # Jika x lebih kecil dari mid
    else:
      high = mid - 1

  return -1

# Contoh penggunaan
arr = [2, 4, 6, 8, 10, 12]
x = 6

result = binary_search_even(arr, x)

if result != -1:
  print("Elemen ditemukan di indeks", str(result))
else:
  print("Elemen tidak ditemukan")