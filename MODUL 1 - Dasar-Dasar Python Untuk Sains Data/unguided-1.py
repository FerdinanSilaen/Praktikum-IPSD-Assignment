def is_prime(num):
  """Mengecek apakah sebuah bilangan adalah prima"""
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def generate_prime_pattern(rows):
  """Menghasilkan pola bilangan prima"""
  primes = [2]
  for i in range(rows):
    count = 0
    for j in range(primes[-1] + 1, 1000):  # Batas atas bisa disesuaikan
      if is_prime(j):
        primes.append(j)
        print(j, end=' ')
        count += 1
      if count == i + 1:
        break
    print()

# Contoh penggunaan
generate_prime_pattern(6)