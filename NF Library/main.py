import random, string
from function import *
    
print("***** SELAMAT DATANG DI NF LIBRARY *****")
while True:
    print("MENU")
    print("[1] Tambah Anggota Baru")
    print("[2] Tambah Buku Baru")
    print("[3] Pinjam Buku")
    print("[4] Kembalikan Buku")
    print("[5] Lihat Data Peminjaman")
    print("[6] Pembayaran Kasir")
    print("[7] Keluar")
    list_nama = []
    pilih = int(input("Masukkan menu pilihan Anda:"))
    if pilih == 1:
        kode = "LIB" + "".join(random.choice(string.digits) for _ in range(3))
        list_nama.append(kode)
        print("*** PENDAFTARAN ANGGOTA BARU ***")
        nama = input("Masukkan nama:")
        if formatNama(nama):
            list_nama.append(nama)
            anggota = input("Apakah merupakan karyawan NF Group? (Y/T):")
            if anggota == "Y":
                tipe = "1" 
                list_nama.append(tipe)
                print("Pendaftaran anggota dengan kode", kode, "atas nama", nama, "berhasil")
                buka_anggota(list_nama)
            else:
                tipe = "2"
                list_nama.append(tipe)
                print("Pendaftaran anggota dengan kode", kode, "atas nama", nama, "berhasil")
                buka_anggota(list_nama)
        else:
            print("Masukkan kode ulang!")
    elif pilih == 2:
        buku = []
        print("*** PENAMBAHAN BUKU BARU ***")
        judul = input("Judul :")
        penulis = input("Penulis :")
        stok = input("Stok :")
        penulis_spasi = penulis.replace(" ","").upper()
        kode_penulis2 = penulis_spasi[0:3] + "".join(random.choice(string.digits)for _ in range(3))
        if penulis[2] == " ":
            buku.append(kode_penulis2)
            buku.append(judul)
            buku.append(penulis)
            buku.append(stok)
            buka_buku(buku)
            print("Penambahan buku baru dengan kode "+ kode_penulis2 + " dan judul", judul, "berhasil")
        else:
            buku.append(kode_penulis2)
            buku.append(judul)
            buku.append(penulis)
            buku.append(stok)
            buka_buku(buku)
            print("Penambahan buku baru dengan kode", kode_penulis2, "dan judul", judul, "berhasil")
    elif pilih == 3:
        print("*** PEMINJAMAN BUKU ***")
        kodebuku = input("kode buku :")
        if bagian_buku(kodebuku):
            kodeanggota = input("kode anggota: ")
            if bagian_anggota(kodeanggota):
                if cek_stok(kodebuku):
                    print("Peminjaman Buku", kodebuku, "oleh", kodeanggota, "berhasil")
                    tulis_peminjaman(kodeanggota,kodebuku)
                    kurang_stok(kodebuku)
                else:
                    print("Stok buku kosong, Peminjaman gagal")
            else:
                print("Kode anggota tidak terdaftar. Peminjaman gagal")
        else:
            print("kode buku tidak ditemukan. Peminjaman gagal")
    elif pilih == 4:
        print("*** PENGEMBALIAN BUKU ***")
        buku_pengembalian = input("Kode Buku :")
        if kodebuku_pengembalian(buku_pengembalian): 
            anggota_pengembalian = input("Kode anggota :")
            if kodeanggota_pengembalian(buku_pengembalian,anggota_pengembalian):
                denda = int(input("keterlambatan pengembalian (dalam hari, 0 jika tidak terlambat) :"))
                if cek_anggotaNF(anggota_pengembalian):
                    denda1 = 1000 * denda
                else:
                    denda1 = 2500 * denda
                hapus_anggota(buku_pengembalian,anggota_pengembalian)
                tambah_anggota(buku_pengembalian)
                print("Total denda = ", denda1)
                print("Silahkan membayar denda keterlambatan di kasir")
                print("Pengembalian buku " + buku_pengembalian +" oleh " + anggota_pengembalian + " berhasil")
            else:
                print("kode anggota tidak terdaftar sebagai peminjam buku tersebut. Pengembalian buku gagal")
        else:
            print("Kode buku salah, pengembalian buku gagal")
    elif pilih == 5:
        data_peminjam()
    elif pilih == 6:
        kasir()
    elif pilih == 7:
        break
    else:
        ("Pilihan anda salah. Ulangi")
print("Terima kasih atas kunjungan Anda...")