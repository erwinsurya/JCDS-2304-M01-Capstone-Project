# Purwadhika JCDS-2304
# M01 - Capstone Project
# Erwin Surya

# --------------------------------- DATA ---------------------------------

datUni = [['iPhone', '14', 'Basic', '64 GB', 'Black', 40],
          ['iPhone', '14', 'Plus', '128 GB', 'Blue', 35],
          ['iPhone', '15', 'Pro', '256 GB', 'Titanium', 30],
          ['iPhone', '15', 'Pro Max', '512 GB', 'Titanium', 25],
          ['iPad', 'Basic', 'Gen 10', '64 GB', 'Silver', 30],
          ['iPad', 'Mini', 'Gen 6', '64 GB', 'Starlight', 25],
          ['iPad', 'Air', 'Gen 5', '256 GB', 'Starlight', 20],
          ['iPad', 'Pro', 'Gen 6', '512 GB', 'Space Gray', 15],
          ['Macbook', 'Air 13"', 'M2', '256 GB', 'Starlight', 20],
          ['Macbook', 'Air 15"', 'M2', '256 GB', 'Silver', 15],
          ['Macbook', 'Pro 14"', 'M3', '512 GB', 'Silver', 10],
          ['Macbook', 'Pro 16"', 'M3', '512 GB', 'Space Gray', 5]]

# datUni = []

# ------------------------------ VALIDATION ------------------------------

dafKol = ['Kategori', 'Seri', 'Tipe', 'Kapasitas', 'Warna', 'Stok']
dafKat = ['iPhone', 'iPad', 'Macbook']
dafSer = ['Basic', '14', '15', 'Mini', 'Air', 'Pro', 'Air 13"', 'Air 15"', 'Pro 14"', 'Pro 16"']
dafTip = ['Basic', 'Plus', 'Pro', 'Pro Max', 'Gen 5', 'Gen 6', 'Gen 9', 'Gen 10', 'M2', 'M3']
dafKap = ['64 GB', '128 GB', '256 GB', '512 GB', '1 TB']
dafWar = ['Black', 'Blue', 'Titanium', 'Silver', 'Space Gray', 'Starlight']

dafIya = ['y', 'ya', 'iya']
dafTdk = ['t', 'tdk', 'tidak']

# ----------------------------- PRETTY TABLE -----------------------------

from prettytable import PrettyTable

# ------------------------------- FUNCTION -------------------------------

def valPil1():
    print()
    print('Karakter input tidak sesuai dengan pilihan yang tersedia. Silakan coba kembali.')

def valPil2():
    print()
    print('Format input tidak valid. Silakan coba kembali.')

def valPil3():
    print()
    print('Data tidak ditemukan. Silakan coba kembali.')

def valPil4():
    print()
    print('Data sudah ada. Silakan coba kembali.')

def funTpl1():
    if len(datUni) > 0:
        tabUni = PrettyTable()
        tabUni.field_names = ['NO', 'DESKRIPSI', 'KAPASITAS', 'WARNA', 'STOK']
        tabUni.align['NO'] = "r"
        tabUni.align['DESKRIPSI'] = "l"
        tabUni.align['KAPASITAS'] = "r"
        tabUni.align['WARNA'] = "l"
        tabUni.align['STOK'] = "r"
        for i in range(len(datUni)):
            tabUni.add_row([i+1, datUni[i][0]+' '+datUni[i][1]+' '+datUni[i][2], datUni[i][3], datUni[i][4], datUni[i][5]])
        print()
        print('DATA UNIT')
        print(tabUni)
    else:
        valPil3()

def funTpl2():
    if len(datUni) > 0:
        while True:
            print()
            inpNom = input('Masukkan Nomor Unit : ')

            try:
                inpNom = int(inpNom)
            except:
                valPil2()
                continue
            
            if inpNom >= 1 and inpNom <= len(datUni):
                tabUni = PrettyTable()
                tabUni.field_names = ['NO', 'DESKRIPSI', 'KAPASITAS', 'WARNA', 'STOK']
                tabUni.align['NO'] = "r"
                tabUni.align['DESKRIPSI'] = "l"
                tabUni.align['KAPASITAS'] = "r"
                tabUni.align['WARNA'] = "l"
                tabUni.align['STOK'] = "r"
                tabUni.add_row([inpNom, datUni[inpNom-1][0]+' '+datUni[inpNom-1][1]+' '+datUni[inpNom-1][2], datUni[inpNom-1][3], datUni[inpNom-1][4], datUni[inpNom-1][5]])
                print()
                print('DATA UNIT')
                print(tabUni)
                break
            else:
                valPil3()
                continue  
    
    else:
        valPil3()

def funTpl3():
    if len(datUni) > 0:
        while True:
            print()
            inpKat = input(f'Masukkan Kategori Unit ({" / ".join(dafKat)}) : ')
            if inpKat in dafKat:
                tabUni = PrettyTable()
                tabUni.field_names = ['NO', 'DESKRIPSI', 'KAPASITAS', 'WARNA', 'STOK']
                tabUni.align['NO'] = "r"
                tabUni.align['DESKRIPSI'] = "l"
                tabUni.align['KAPASITAS'] = "r"
                tabUni.align['WARNA'] = "l"
                tabUni.align['STOK'] = "r"
                x = 0
                for i in range(len(datUni)):
                    if datUni[i][0] == inpKat:
                        x += 1
                        tabUni.add_row([i+1, datUni[i][0]+' '+datUni[i][1]+' '+datUni[i][2], datUni[i][3], datUni[i][4], datUni[i][5]])
                if x > 0:
                    print()
                    print('DATA UNIT')
                    print(tabUni)
                    break
                else:
                    valPil3()
                    break
            else:
                valPil1()
                continue
    
    else:
        valPil3()

def funTbh():
    while True:
        print()
        inpNom = input('Masukkan Nomor Unit : ')

        try:
            inpNom = int(inpNom)
        except:
            valPil2()
            continue

        if inpNom > len(datUni):
            while True:
                print()
                inpKat = input(f'Masukkan Kategori Unit ({" / ".join(dafKat)}) : ')
                if inpKat in dafKat:
                    while True:
                        print()
                        inpSer = input(f'Masukkan Seri Unit ({" / ".join(dafSer)}) : ')
                        if inpSer in dafSer:
                            while True:
                                print()
                                inpTip = input(f'Masukkan Tipe Unit ({" / ".join(dafTip)}) : ')
                                if inpTip in dafTip:
                                    while True:
                                        print()
                                        inpKap = input(f'Masukkan Kapasitas Unit ({" / ".join(dafKap)}) : ')
                                        if inpKap in dafKap:
                                            while True:
                                                print()
                                                inpWar = input(f'Masukkan Warna Unit ({" / ".join(dafWar)}) : ')
                                                if inpWar in dafWar:
                                                    while True:
                                                        print()
                                                        inpSto = input(f'Masukkan Stok Unit (1-100) : ')

                                                        try:
                                                            inpSto = int(inpSto)
                                                        except:
                                                            valPil2()
                                                            continue

                                                        if inpSto >= 1 and inpSto <= 100:
                                                            break
                                                        else:
                                                            valPil1()
                                                            continue
                                                    break
                                                else:
                                                    valPil1()
                                                    continue
                                            break
                                        else:
                                            valPil1()
                                            continue
                                    break
                                else:
                                    valPil1()
                                    continue
                            break
                        else:
                            valPil1()
                            continue
                    break
                else:
                    valPil1()
                    continue
            
            tabUni = PrettyTable()
            tabUni.field_names = ['NO', 'DESKRIPSI', 'KAPASITAS', 'WARNA', 'STOK']
            tabUni.align['NO'] = "r"
            tabUni.align['DESKRIPSI'] = "l"
            tabUni.align['KAPASITAS'] = "r"
            tabUni.align['WARNA'] = "l"
            tabUni.align['STOK'] = "r"
            tabUni.add_row([inpNom, inpKat+' '+inpSer+' '+inpTip, inpKap, inpWar, inpSto])
            print()
            print('DATA UNIT')
            print(tabUni)
            
            while True:
                print()
                cekPil = input('Apakah Anda ingin menyimpan data ini? (Y/T) : ')
                if cekPil.lower() in dafIya:
                    datUni.append([inpKat, inpSer, inpTip, inpKap, inpWar, inpSto])
                    print()
                    print('Data berhasil disimpan.')
                    break
                elif cekPil.lower() in dafTdk:
                    print()
                    print('Data batal disimpan.')
                    break
                else:
                    valPil1()
                    continue
            break
        
        else:
            valPil4()
            break
        
def funUba():
    while True:
        print()
        inpNom = input('Masukkan Nomor Unit : ')

        try:
            inpNom = int(inpNom)
        except:
            valPil2()
            continue
        
        if inpNom >= 1 and inpNom <= len(datUni):
            tabUni = PrettyTable()
            tabUni.field_names = ['NO', 'DESKRIPSI', 'KAPASITAS', 'WARNA', 'STOK']
            tabUni.align['NO'] = "r"
            tabUni.align['DESKRIPSI'] = "l"
            tabUni.align['KAPASITAS'] = "r"
            tabUni.align['WARNA'] = "l"
            tabUni.align['STOK'] = "r"
            tabUni.add_row([inpNom, datUni[inpNom-1][0]+' '+datUni[inpNom-1][1]+' '+datUni[inpNom-1][2], datUni[inpNom-1][3], datUni[inpNom-1][4], datUni[inpNom-1][5]])
            print()
            print('DATA UNIT')
            print(tabUni)

            while True:
                print()
                cekPil = input('Apakah Anda ingin melanjutkan? (Y/T) : ')
                if cekPil.lower() in dafIya:
                    while True:
                        print()
                        inpKol = input(f'Masukkan Nama Kolom ({" / ".join(dafKol)}) : ')
                        if inpKol in dafKol:
                            while True:
                                if inpKol == 'Kategori':
                                    print()
                                    inpNil = input(f'Masukkan Nilai Baru ({" / ".join(dafKat)}) : ')
                                    if inpNil in dafKat:
                                        indKol = 0
                                        break
                                    else:
                                        valPil1()
                                        continue
                                elif inpKol == 'Seri':
                                    print()
                                    inpNil = input(f'Masukkan Nilai Baru ({" / ".join(dafSer)}) : ')
                                    if inpNil in dafSer:
                                        indKol = 1
                                        break
                                    else:
                                        valPil1()
                                        continue
                                elif inpKol == 'Tipe':
                                    print()
                                    inpNil = input(f'Masukkan Nilai Baru ({" / ".join(dafTip)}) : ')
                                    if inpNil in dafTip:
                                        indKol = 2
                                        break
                                    else:
                                        valPil1()
                                        continue
                                elif inpKol == 'Kapasitas':
                                    print()
                                    inpNil = input(f'Masukkan Nilai Baru ({" / ".join(dafKap)}) : ')
                                    if inpNil in dafKap:
                                        indKol = 3
                                        break
                                    else:
                                        valPil1()
                                        continue
                                elif inpKol == 'Warna':
                                    print()
                                    inpNil = input(f'Masukkan Nilai Baru ({" / ".join(dafWar)}) : ')
                                    if inpNil in dafWar:
                                        indKol = 4
                                        break
                                    else:
                                        valPil1()
                                        continue
                                else:
                                    print()
                                    inpNil = input(f'Masukkan Nilai Baru (1-100) : ')

                                    try:
                                        inpNil = int(inpNil)
                                    except:
                                        valPil2()
                                        continue

                                    if inpNil >= 1 and inpNil <= 100:
                                        indKol = 5
                                        break
                                    else:
                                        valPil1()
                                        continue
                            break                     
                        else:
                            valPil1()
                            continue
                    
                    tabUni = PrettyTable()
                    tabUni.field_names = ['NO', 'DESKRIPSI', 'KAPASITAS', 'WARNA', 'STOK']
                    tabUni.align['NO'] = "r"
                    tabUni.align['DESKRIPSI'] = "l"
                    tabUni.align['KAPASITAS'] = "r"
                    tabUni.align['WARNA'] = "l"
                    tabUni.align['STOK'] = "r"
                    if indKol == 0:
                        tabUni.add_row([inpNom, inpNil+' '+datUni[inpNom-1][1]+' '+datUni[inpNom-1][2], datUni[inpNom-1][3], datUni[inpNom-1][4], datUni[inpNom-1][5]])
                    elif indKol == 1:
                        tabUni.add_row([inpNom, datUni[inpNom-1][0]+' '+inpNil+' '+datUni[inpNom-1][2], datUni[inpNom-1][3], datUni[inpNom-1][4], datUni[inpNom-1][5]])
                    elif indKol == 2:
                        tabUni.add_row([inpNom, datUni[inpNom-1][0]+' '+datUni[inpNom-1][1]+' '+inpNil, datUni[inpNom-1][3], datUni[inpNom-1][4], datUni[inpNom-1][5]])
                    elif indKol == 3:
                        tabUni.add_row([inpNom, datUni[inpNom-1][0]+' '+datUni[inpNom-1][1]+' '+datUni[inpNom-1][2], inpNil, datUni[inpNom-1][4], datUni[inpNom-1][5]])
                    elif indKol == 4:
                        tabUni.add_row([inpNom, datUni[inpNom-1][0]+' '+datUni[inpNom-1][1]+' '+datUni[inpNom-1][2], datUni[inpNom-1][3], inpNil, datUni[inpNom-1][5]])
                    else:
                        tabUni.add_row([inpNom, datUni[inpNom-1][0]+' '+datUni[inpNom-1][1]+' '+datUni[inpNom-1][2], datUni[inpNom-1][3], datUni[inpNom-1][4], inpNil])
                    print()
                    print('DATA UNIT')
                    print(tabUni)
                    
                    while True:
                        print()
                        cekPil = input('Apakah Anda ingin mengubah data ini? (Y/T) : ')
                        if cekPil.lower() in dafIya:
                            datUni[inpNom-1][indKol] = inpNil
                            print()
                            print('Data berhasil diubah.')
                            break
                        elif cekPil.lower() in dafTdk:
                            print()
                            print('Data batal diubah.')
                            break
                        else:
                            valPil1()
                            continue
                    break
                elif cekPil.lower() in dafTdk:
                    print()
                    print('Anda batal melanjutkan.')
                    break
                else:
                    valPil1()
                    continue
            break
        
        else:
            valPil3()
            break

def funHap():
    while True:
        print()
        inpNom = input('Masukkan Nomor Unit : ')

        try:
            inpNom = int(inpNom)
        except:
            valPil2()
            continue
        
        if inpNom >= 1 and inpNom <= len(datUni):
            tabUni = PrettyTable()
            tabUni.field_names = ['NO', 'DESKRIPSI', 'KAPASITAS', 'WARNA', 'STOK']
            tabUni.align['NO'] = "r"
            tabUni.align['DESKRIPSI'] = "l"
            tabUni.align['KAPASITAS'] = "r"
            tabUni.align['WARNA'] = "l"
            tabUni.align['STOK'] = "r"
            tabUni.add_row([inpNom, datUni[inpNom-1][0]+' '+datUni[inpNom-1][1]+' '+datUni[inpNom-1][2], datUni[inpNom-1][3], datUni[inpNom-1][4], datUni[inpNom-1][5]])
            print()
            print('DATA UNIT')
            print(tabUni)

            while True:
                print()
                cekPil = input('Apakah Anda ingin menghapus data ini? (Y/T) : ')
                if cekPil.lower() in dafIya:
                    del datUni[inpNom-1]
                    print()
                    print('Data berhasil dihapus.')
                    break
                elif cekPil.lower() in dafTdk:
                    print()
                    print('Data batal dihapus.')
                    break
                else:
                    valPil1()
                    continue
            break
        
        else:
            valPil3()
            break

# --------------------------------- MENU ---------------------------------

while True:
    print()
    print('Selamat Datang di Gudang iBoks')
    print()
    print('MENU UTAMA')
    print('1. Penampilan Data')
    print('2. Penambahan Data')
    print('3. Pengubahan Data')
    print('4. Penghapusan Data')
    print('5. Keluar Program')
    print()
    menUta = input('Masukkan Pilihan Anda (1-5) : ')

    if menUta == '1':
        while True:
            print()
            print('SUBMENU 1')
            print('1. Menampilkan Semua Unit')
            print('2. Menampilkan Unit Berdasarkan Nomor')
            print('3. Menampilkan Unit Berdasarkan Kategori')
            print('4. Kembali ke Menu Utama')
            print()
            menSub = input('Masukkan Pilihan Anda (1-4) : ')

            if menSub == '1':
                funTpl1()
            elif menSub == '2':
                funTpl2()
            elif menSub == '3':
                funTpl3()
            elif menSub == '4':
                break
            else:
                valPil1()
                continue  

    elif menUta == '2':
        while True:
            print()
            print('SUBMENU 2')
            print('1. Menambah Unit')
            print('2. Kembali ke Menu Utama')
            print()
            menSub = input('Masukkan Pilihan Anda (1-2) : ')

            if menSub == '1':
                funTbh()
            elif menSub == '2':
                break
            else:
                valPil1()
                continue  
            
    elif menUta == '3':
        while True:
            print()
            print('SUBMENU 3')
            print('1. Mengubah Unit')
            print('2. Kembali ke Menu Utama')
            print()
            menSub = input('Masukkan Pilihan Anda (1-2) : ')

            if menSub == '1':
                funUba()
            elif menSub == '2':
                break
            else:
                valPil1()
                continue  
            
    elif menUta == '4':
        while True:
            print()
            print('SUBMENU 4')
            print('1. Menghapus Unit')
            print('2. Kembali ke Menu Utama')
            print()
            menSub = input('Masukkan Pilihan Anda (1-2) : ')

            if menSub == '1':
                funHap()
            elif menSub == '2':
                break
            else:
                valPil1()
                continue  
            
    elif menUta == '5':
        print()
        print('Anda telah keluar dari program.')
        print()
        break

    else:
        valPil1()
        continue  

# ------------------------------- GLOSSARY -------------------------------
    
# datUni : Data Unit
# tabUni : Tabel Unit

# menUta : Menu Utama
# menSub : Menu Sub

# funTpl : Fungsi Tampil
# funTbh : Fungsi Tambah
# funUba : Fungsi Ubah
# funHap : Fungsi Hapus

# dafKol : Daftar Kolom
# dafKat : Daftar Kategori
# dafSer : Daftar Seri
# dafTip : Daftar Tipe
# dafKap : Daftar Kapasitas
# dafWar : Daftar Warna

# dafIya : Daftar Iya
# dafTdk : Daftar Tidak

# cekPil : Cek Pilihan
# valPil : Validasi Pilihan

# inpNom : Input Nomor
# inpKat : Input Kategori
# inpSer : Input Seri
# inpTip : Input Tipe
# inpKap : Input Kapasitas
# inpWar : Input Warna
# inpSto : Input Stok
# inpNil : Input Nilai

# indKol : Indeks Kolom
