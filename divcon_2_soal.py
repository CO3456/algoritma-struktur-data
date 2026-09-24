# Data mahasiswa dan 5 nilai UG
mahasiswa = [
    {"nama": "Andi", "nilai": [80, 75, 90, 70, 85]},
    {"nama": "Budi", "nilai": [60, 65, 70, 55, 60]},
    {"nama": "Citra", "nilai": [90, 85, 95, 88, 92]},
    {"nama": "Deni", "nilai": [70, 75, 65, 72, 68]},
    {"nama": "Eka", "nilai": [85, 80, 78, 90, 87]},
    {"nama": "Fajar", "nilai": [65, 70, 68, 60, 72]},
    {"nama": "Gina", "nilai": [88, 92, 85, 90, 87]},
    {"nama": "Hadi", "nilai": [75, 80, 70, 78, 72]},
    {"nama": "Intan", "nilai": [55, 60, 65, 58, 62]},
    {"nama": "Joko", "nilai": [78, 82, 75, 80, 85]}
]


# Menghitung rata-rata nilai setiap mahasiswa
for mhs in mahasiswa:
    mhs["rata-rata"] = sum(mhs["nilai"]) / len(mhs["nilai"])



# Divide and Conquer - Merge Sort
def merge_sort(data):
    if len(data) <= 1:
        return data
#divide 
    mid = len(data)//2
    kiri = data[:mid]
    kanan = data[mid:]
#conquer
    kiri = merge_sort(kiri)
    kanan = merge_sort(kanan)
#combine
    return merge(kiri, kanan)


def merge(kiri, kanan):
    hasil = []
    i = 0 
    j = 0 
#mengurutkan dari yang terbesar ke terkecil
    while i < len(kiri) and j < len(kanan):
        if kiri[i]["rata-rata"] >= kanan[j]["rata-rata"]:
            hasil.append(kiri[i])
            i += 1 
        else: 
            hasil.append(kanan[j])
            j += 1
    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])
    return hasil


# Menghitung rata-rata keseluruhan
total_rata_rata = 0 

for mhs in mahasiswa:
    total_rata_rata += mhs["rata-rata"]

rata_rata_keseluruhan = total_rata_rata / len(mahasiswa)


# Mengurutkan mahasiswa menggunakan Merge Sort
mahasiswa_urut = merge_sort(mahasiswa)
print(rata_rata_keseluruhan)

# Menampilkan hasil rata-rata keseluruhan

print("\n=== DI ATAS / SAMA DENGAN RATA-RATA ===")
nomor = 1 
for mhs in mahasiswa_urut:
    if mhs["rata-rata"] >= rata_rata_keseluruhan:
        print(
            nomor,
            mhs["nama"],
            "Nilai", mhs["nilai"],
            "rata-rata", mhs["rata-rata"]
        )
        nomor += 1 

# Tampilkan List di atas / sama dengan rata-rata


print("\n=== DI BAWAH RATA-RATA ===")
nomor = 1
for mhs in mahasiswa_urut:
    if mhs["rata-rata"] < rata_rata_keseluruhan:
        print(
            nomor, 
            mhs["nama"],
            "Nilai", mhs["nilai"],
            "rata-rata", mhs["rata-rata"]
        )
        nomor += 1         

# Tampilkan List di bawah rata-rata