# 8. Buat sebuah program yang menerima string dari pengguna dan mengonversi string tersebut menjadi sebuah list berisi kata-kata terbalik. Misalnya:

#Input: "Saya suka Python"
#Output: ["ayaS", "akus", "nohtyP"]

def kata_terbalik(string):
    kata_list = string.split()

    kata_terbalik_list = [kata[::-1] for kata in kata_list]
    
    return kata_terbalik_list

input_string = input("Masukkan string: ")
hasil = kata_terbalik(input_string)

print(hasil)
