# 1. Buatlah program yang dapat menghasilkan pola berbentuk angka seperti di bawah ini,
# dengan syarat angka yang ditampilkan adalah hasil dari penjumlahan bilangan prima sebelumnya

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_pattern(n_rows):
    primes = [] 
    num = 2 
    for row in range(1, n_rows + 1):
        row_primes = [] 
        while len(row_primes) < row:
            if is_prime(num):
                row_primes.append(num)
            num += 1
        primes.append(row_primes)

    return primes

def display_prime_pattern(n_rows):
    prime_pattern = generate_prime_pattern(n_rows)
    for row in prime_pattern:
        print(" ".join(map(str, row)))

display_prime_pattern(5)
