def masukkan_nilai_siswa(jumlah_siswa):
    data_siswa = {}
    for _ in range(jumlah_siswa):
        nama = input("Masukkan nama siswa: ")
        nilai = int(input("Masukkan nilai siswa: "))
        data_siswa[nama] = nilai
    return data_siswa

try:
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    grade = masukkan_nilai_siswa(jumlah_siswa)
    print("Kamus nilai siswa:", grade)
except ValueError:
    print("Masukkan harus berupa bilangan bulat.")
