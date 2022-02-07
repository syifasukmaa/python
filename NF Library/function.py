# Fungsi Fitur 1
def buka_anggota(list_nama):
    output_file = open("anggota.txt", 'a')
    output_file.write("\n" + list_nama[0] + "," + list_nama[1] + "," + list_nama[2])
    output_file.close()

def formatNama(nama):
    nama = nama.split(" ")
    cek = 0
    for i in nama:
        if i[0].isupper():
            cek +=1    
    if cek == len(nama):
        return True
    else:
        return False
    
# Fungsi Fitur 2
def buka_buku(buku):
    output_buku = open("buku.txt", 'a')
    output_buku.write("\n" + buku[0] + "," + buku[1] + "," + buku[2] + "," + buku[3] )
    output_buku.close()
    
# Fungsi Fitur 3
def baca_bukuu():
    data_buku = []
    f = open('buku.txt')
    for each_line in f:
        data_buku.append(each_line.strip())
    f.close()
    return data_buku

def peminjaman():
    data_buku = []
    f = open("peminjaman.txt")
    for each_line in f:
        data_buku.append(each_line.strip())
    f.close()
    return data_buku

def anggota():
    data_buku = []
    f = open("anggota.txt")
    for i in f:
        data_buku.append(i.strip())
    f.close()
    return data_buku

def bagian_buku(kodebuku):
    for i in baca_bukuu():
        if i[:6] == kodebuku:
            return True
    return False

def bagian_anggota(kodeanggota):
    for i in anggota():
        if i[:6] == kodeanggota:
            return True
    return False

def cek_stok(kodebuku):
    data = baca_bukuu()
    for i in range(len(data)):
        if data[i][:6] == kodebuku:
            data[i] = data[i].split(",")
            if int(data[i][-1]) > 0:
                return True
    return False

def tulis_peminjaman(kodeanggota,kodebuku): #memasukkan data yang dipinjam
    data_buku = peminjaman()
    ada = 0
    for i in range(len(data_buku)):
        if data_buku[i][:6] == kodebuku:
            data_buku[i] = data_buku[i] + "," + kodeanggota #KALAU SUDAH ADA ANGGOTA
            ada = 1
    if ada == 1:
        f = open("peminjaman.txt", "w+")
        for i in data_buku:
            f.write(i + "\n")
        f.close()
    else:
        f = open("peminjaman.txt", "a+")
        f.write(kodebuku + "," + kodeanggota + "\n")
        f.close()

def kurang_stok(kodebuku): 
    data_buku = baca_bukuu()
    for i in range(len(data_buku)):
        if data_buku[i][:6] == kodebuku:
            data_buku[i] = data_buku[i].split(",")
            data_buku[i][-1] = str(int(data_buku[i][-1]) - 1)
            data_buku[i] = ",".join(data_buku[i])
    f = open("buku.txt", "w+")
    for i in data_buku:
        f.write(i + "\n")
    f.close()
    
# Fungsi Fitur 4
def kodebuku_pengembalian(buku_pengembalian):
    data_buku = peminjaman()
    for i in range(len(data_buku)):
        if data_buku[i][:6] == buku_pengembalian:
            data_buku[i] = data_buku[i].split(",")
            return True
    return False

def kodeanggota_pengembalian(buku_pengembalian,anggota_pengembalian):
    data_buku = peminjaman()
    for i in range(len(data_buku)):
        if data_buku[i][:6] == buku_pengembalian:
            data_buku[i] = data_buku[i].split(",")
            if data_buku[i].count(anggota_pengembalian) > 0: #karena jika ada 2 anggota yang sama akan tetap berjalan
                return True
            return False
                
def hapus_anggota(buku_pengembalian,anggota_pengembalian):
    data_buku = peminjaman()
    for i in range(len(data_buku)):
        if data_buku[i][:6] == buku_pengembalian:
            data_buku[i] = data_buku[i].split(",")
            data_buku[i].remove(anggota_pengembalian) #menghapus kode anggota yang ada
            if len(data_buku[i]) == 1:
                del data_buku[i] #menghapus kodebukunya juga
            else:
                data_buku[i] = ",".join(data_buku[i]) #ngembaliin jadi string lagi
    file_open = open("peminjaman.txt", "w+")
    for i in data_buku:
        file_open.write(i +"\n")
    file_open.close()

def cek_anggotaNF(anggota_pengembalian):
    data_buku = anggota()
    for i in range(len(data_buku)):
        if data_buku[i][:6] == anggota_pengembalian:
            if data_buku[i][-1] =="1":
                return True
            else:
                return False
            
def tambah_anggota(buku_pengembalian):
    data_buku = baca_bukuu()
    for i in range(len(data_buku)):
        if data_buku[i][:6] == buku_pengembalian:
            data_buku[i] = data_buku[i].split(",")
            data_buku[i][-1] = str(int(data_buku[i][-1]) + 1)
            data_buku[i] = ",".join(data_buku[i])
    open_file= open("buku.txt", "w+")
    for i in data_buku:
        open_file.write(i + "\n")
    open_file.close()
    
#Fitur 5
def data_peminjam():
    temp = []
    databuku = {}
    f = open("buku.txt")
    for i in f:
        temp = i.strip().split(",")
        databuku[temp[0]] = temp[1:]

    temp = []
    datapeminjaman ={}
    f = open("peminjaman.txt")
    for i in f:
        temp = i.strip().split(",")
        datapeminjaman[temp[0]] = temp[1:]

    temp = []
    dataanggota ={}
    f = open("anggota.txt")
    for i in f:
        temp = i.strip().split(",")
        dataanggota[temp[0]] = temp[1:]

    print("*** DAFTAR PEMINJAMAN BUKU ***\n")

    for i in datapeminjaman.keys(): 
        nomer = 0
        print("Judul : "+databuku[i][0])
        print("Penulis : "+databuku[i][1])
        print("Daftar Pinjam:")
        for j in datapeminjaman[i]: #datapeminjaman[i] ini merupakan value dari si i yang dimana i merupakan keys dari data peminjaman
            nomer += 1
            if dataanggota[j][1] == "1":
                print(str(nomer) + ".", dataanggota[j][0] + "(*)")#nah ini ngeprint value dari dataanggota yang keysnya itu dari j
            else:
                print(str(nomer) + ".", dataanggota[j][0])
        print()
#Fitur 6
def kasir():
    anggota_pengembalian = input("Kode anggota :")
    denda = int(input("keterlambatan pengembalian (dalam hari, 0 jika tidak terlambat) :"))
    if cek_anggotaNF(anggota_pengembalian):
        jml_denda = 1000 * denda 
        print(jml_denda)
        uang = abs(int(input("masukkan jumlah uang yang ingin dibayar :")))
        jumlah = abs(uang - jml_denda)
    else:
        jml_denda = 2500 * denda 
        print(jml_denda)
        uang = abs(int(input("masukkan jumlah uang yang ingin dibayar :")))
        jumlah = abs(uang - jml_denda)
    print("Pengembalian uang =", jumlah)