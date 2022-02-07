import re

akhir = ('Terima kasih telah berbelanja di NFElectrics')
total_barang = 0
total_harga= 0

while True:
    barang = input("Masukkan nama produk yang dibeli atau X untuk selesai:")
    if (barang != "X"):
        harga = float(input("Harga barang:"))
        print("Berhasil menambahkan", barang, "dengan harga", harga)
        total_barang = total_barang + 1
    else:
        break
    total_harga = total_harga + harga
print("")
print("Total produk yang dibeli:", total_barang,
      "\n" + "Total harga produk:", total_harga, "\n")

if total_barang != 0:
    anggota = input('Apakah anda anggota? (Y/T):')
    if anggota == 'Y':
        Pattern = ("^\w+@\w+\.+com+$")
        def checkEmail(address):
            if (re.search(Pattern, address)):
                return address
        while True:                
            email = input('Masukkan email:')
            if not checkEmail(email):
                print('Email tidak valid. Ulangi.')
            else:
                True
                break

        pola = ("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#!@$]).{8,}$")
        def checkPass(pwd):
            if (re.search(pola, pwd)):
                return pwd
        while True:                
            sandi = input('Masukkan Password:')
            if not checkPass(sandi):
                print('Email tidak valid. Ulangi.')
            else:
                True
                break

        while True:
            peserta = input('Masukkan level kepesertaan Anda:')
            diskon_10 = ('10%')
            diskon_15 = ('15%')
            diskon_5 = ('5%')
            diskon_20 = ('20%')
            if peserta == "Gold":
                if total_barang < 5:
                    diskon = total_harga * (10/100)
                    sesudah_diskon = total_harga - diskon
                    print('Selamat! Anda mendapat potongam harga', diskon_10)
                    print('Total harga yang harus dibayar:', sesudah_diskon)
                    print(akhir)
                    break
                else:
                    diskon = total_harga * (15/100)
                    sesudah_diskon = total_harga - diskon
                    print('Selamat! Anda mendapat potongam harga', diskon_15)
                    print('Total harga yang harus dibayar:', sesudah_diskon)
                    print(akhir)
                    break
            elif peserta == "Silver":
                if total_barang < 5:
                    diskon = total_harga * (5/100)
                    sesudah_diskon = total_harga - diskon
                    print('Selamat! Anda mendapat potongam harga', diskon_5)
                    print(sesudah_diskon)
                    print(akhir)
                    break
                else:
                    diskon = total_harga * (10/100)
                    sesudah_diskon = total_harga - diskon
                    print('Selamat! Anda mendapat potongam harga', diskon_10)
                    print(sesudah_diskon)
                    print(akhir)
                    break
            elif peserta == "Diamond":
                if total_barang < 5:
                    diskon = total_harga * (15/100)
                    sesudah_diskon = total_harga - diskon
                    print('Selamat! Anda mendapat potongam harga', diskon_15)
                    print(sesudah_diskon)
                    print(akhir)
                    break
                else:
                    diskon = total_harga * (20/100)
                    sesudah_diskon = total_harga - diskon
                    print('Selamat! Anda mendapat potongam harga', diskon_20)
                    print(sesudah_diskon)
                    print(akhir)
                    break
            else:
                print('Masukkan tidak valid. Ulangi')
                continue
    else:
        print('Total harga yang harus anda bayar:', total_harga, 
            "\n" + akhir)