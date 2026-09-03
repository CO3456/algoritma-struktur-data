def pola_sakit_kepala(panjang, lebar):
    panjang == abs (panjang)
    lebar  == abs (lebar)
    
    if panjang != lebar:
        print("panjang dan lebar harus sama!")
        return

    if panjang % 2 == 0 or lebar % 2 == 0:
        print("panjang dan lebar harus ganjil!")
        return
    
    
    n = panjang 
    pusat = n // 2 

    for i in range(panjang):
        for j in range(lebar):
            nilai = (abs(i - pusat) + abs(j - pusat)) + 1
            

            if j == lebar - 1:
                print(nilai, end=" ")
            else: 
                print(nilai, end=" ")
        print()

print("no 1. (pola 7,7)")
pola_sakit_kepala(7, 7)
print()
print("no 2. (Pola 4, 4)")
pola_sakit_kepala(4, 4)
print()
print("no 3. (Pola -15, 15)")
pola_sakit_kepala(-15, 15)