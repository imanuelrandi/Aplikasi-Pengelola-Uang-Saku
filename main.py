saldo = 0

def tambah_pemasukan():
    global saldo
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    saldo += jumlah
    print(f"Pemasukan berhasil ditambahkan! Saldo sekarang: {saldo}")

def tambah_pengeluaran():
    global saldo
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    if jumlah > saldo:
        print("Peringatan! Saldo tidak cukup!")
    else:
        saldo -= jumlah
        print(f"Pengeluaran berhasil dicatat! Saldo sekarang: {saldo}")

def lihat_saldo():
    print("=" * 30)
    print(f"Saldo Anda: Rp {saldo:,.0f}")
    print("=" * 30)

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")
