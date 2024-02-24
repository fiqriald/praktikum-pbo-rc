def tulis_ke_file(nama_file):
    with open(nama_file, 'w') as file:
        file.write("Nama : fiqri aldiansyah\n")
        file.write("NIM : 122140152\n")
        file.write("Resolusi Saya di Tahun ini : sukses di crypto currency\n")

try:
    nama_file = "Me.txt"
    tulis_ke_file(nama_file)
    print(f"File '{nama_file}' berhasil dibuat dan diisi.")
except Exception as e:
    print("Terjadi kesalahan:", str(e))
