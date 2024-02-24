def cetak_segitiga(tinggi):
    for i in range(1, tinggi + 1):
        print(' ' * (tinggi - i) + '*' * (2*i - 1))

try:
    tinggi = int(input("Masukkan tinggi segitiga: "))
    cetak_segitiga(tinggi)
except ValueError:
    print("Masukkan harus berupa bilangan bulat.")
