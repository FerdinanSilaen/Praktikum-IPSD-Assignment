# 4 Anda diberikan file CSV berisi data nilai ujian mahasiswa. Tugas Anda adalah menulis sebuah program yang:
#a. Membaca file CSV dan menyimpan datanya ke dalam dictionary.
#b. Menghitung rata-rata nilai tiap mahasiswa.
#c. Menampilkan mahasiswa dengan nilai tertinggi dan terendah.

import csv

# Membaca file CSV dan menyimpan datanya ke dalam dictionary
def read_csv(file_path):
    student_scores = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  
        for row in csv_reader:
            name = row[0]
            scores = list(map(float, row[1:]))  
            student_scores[name] = scores
    return student_scores

# Menghitung rata-rata nilai tiap mahasiswa
def calculate_averages(student_scores):
    averages = {name: sum(scores) / len(scores) for name, scores in student_scores.items()}
    return averages

# Menemukan semua mahasiswa dengan nilai tertinggi dan terendah
def find_highest_lowest(averages):
    highest_score = max(averages.values())
    lowest_score = min(averages.values())
    
    # Mendapatkan semua siswa dengan nilai rata-rata tertinggi dan terendah
    highest_students = [name for name, avg in averages.items() if avg == highest_score]
    lowest_students = [name for name, avg in averages.items() if avg == lowest_score]
    
    return highest_students, highest_score, lowest_students, lowest_score

# File path
file_path = 'C:/Users/USER/Downloads/siswa_nilai (1).csv'

# Memproses file CSV
student_scores = read_csv(file_path)

# Menghitung rata-rata nilai setiap mahasiswa
averages = calculate_averages(student_scores)

# Menampilkan semua mahasiswa dengan nilai tertinggi dan terendah
highest_students, highest_score, lowest_students, lowest_score = find_highest_lowest(averages)

# Output rata-rata nilai setiap mahasiswa
print("Rata-rata nilai setiap mahasiswa:")
for student, avg in averages.items():
    print(f"{student}: {avg:.2f}")  # Format dengan 2 desimal

# Output mahasiswa dengan nilai tertinggi dan terendah
print(f"\nMahasiswa dengan nilai tertinggi (rata-rata {highest_score:.2f}):")
for student in highest_students:
    print(f"- {student}")

print(f"\nMahasiswa dengan nilai terendah (rata-rata {lowest_score:.2f}):")
for student in lowest_students:
    print(f"- {student}")


