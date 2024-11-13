a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
print("Pilih operasi yang ingin dilakukan:")
print("1. a + b")
print("2. a - b")
print("3. a * b")
pilihan = input("Masukkan pilihan (1/2/3): ")
if pilihan == '1':
        hasil = a + b
        print(f"Hasil a + b = {hasil}")
elif pilihan == '2':
        hasil = a - b
        print(f"Hasil a - b = {hasil}")
elif pilihan == '3':
        hasil = a * b
        print(f"Hasil a * b = {hasil}")
else:
        print("Pilihan tidak valid!")

print("Program selesai.")