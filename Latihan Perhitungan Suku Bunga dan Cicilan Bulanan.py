#Note : Menu Login 1 = Ada pemilihan Login/Register
#       Menu Login 2 = Hanya Looping Login

#Deklarasi Variabel
polis_asuransi = 40000
administrasi = 700000
userpass = {"admin":"1234"}

def login():
    print("Berikut merupakan menu login ICL MOTOGARAGE")
    print("Ketik 1. untuk Login")
    print("Ketik 2. untuk Register")
    return str(input("Masukkan pilihan anda: ")) 

def update():
    #Sistem Menu Pemilihan 2
    print(" ")
    print("="*50)
    print(" "*20,"MAIN MENU")
    print("="*50)
    print(f"Biaya Polis Asuransi saat ini\t: Rp {polis_asuransi}")
    print(f"Biaya Administrasi saat ini\t: Rp {administrasi}")
    print(" ")
    print("Silahkan pilih menu yang anda inginkan")
    print("Ketik 1. untuk Perhitungan Biaya")
    print("Ketik 2. untuk Update Biaya Admin dan Polis Asuransi")
    return str(input("Masukkan pilihan anda: "))

def perhitungan_biaya ():
    print(" ")
    print("="*50)
    print(" "*3,"PERHITUNGAN SUKU BUNGA DAN CICILAN BULANAN")
    print("="*50)
    harga_mobil = int(input("Masukkan Harga Mobil\t\t: "))
    tenor = int(input("Masukkan Tenor(dalam bulan)\t: "))
    DP = float(input("Masukkan Down Payment\t\t: "))
    suku_bunga = float(input("Masukkan Suku Bunga\t\t: "))
    uang_muka = DP * harga_mobil

    #Plafon Pinjaman                
    plafon_pinjaman = int(harga_mobil - (uang_muka/100))

    #Angsuran Pokok Bulanan
    angsuran_pokok = int(plafon_pinjaman/tenor)

    #Angsuran Bunga Bulanan
    angsuran_bunga = int(plafon_pinjaman * suku_bunga/1200)

    #Total Cicilan Bulanan
    total_cicilan = angsuran_pokok + angsuran_bunga

    #Pembayaran Pertama Kali
    asuransi = 5/100 * harga_mobil
    provisi = 5/1000 * plafon_pinjaman
    pembayaran_pertama = int((uang_muka/100) + total_cicilan + asuransi + provisi + polis_asuransi + administrasi)
    
    #Output
    print(" ")
    print("="*50)
    print(" "*16,"HASIL PERHITUNGAN")
    print("="*50)
    print("Plafon Pinjaman\t\t: Rp",(plafon_pinjaman))
    print("Angsuran Pokok Perbulan\t: Rp",(angsuran_pokok))
    print("Angsuran Bunga Perbulan\t: Rp",(angsuran_bunga))
    print("Total Cicilan Perbulan\t: Rp",(total_cicilan))
    print("Pembayaran Pertama Kali\t: Rp",(pembayaran_pertama))

#Sistem Menu Pemilihan
print("="*50)
print(" "*7,"MENU PEMILIHAN LOGIN DAN REGISTER")
print("="*50)
relog = login()

#Pemilihan
if relog == "1" :       #Buat Login
    login = True
    loop = False
elif relog == "2" :     #Buat Register
    login = False
    loop = False
else :                  #Buat Eror Handling
    print(" ")
    print("="*50)
    print(" "*1,"Input SALAH, Mohon Masukkan Pilihan Yang BENAR")
    print("="*50)
    loop = True

#Sistem Looping Menu Pemilihan
while loop == True :
    print(" ")
    print("="*50)
    print(" "*7,"MENU PEMILIHAN LOGIN DAN REGISTER")
    print("="*50)
    relog = login()
    if relog == "1" :
        login = True
        loop = False
    elif relog == "2" :
        login = False
        loop = False
    else :
        print(" ")
        print("="*50)
        print(" "*1,"Input SALAH, Mohon Masukkan Pilihan Yang BENAR")
        print("="*50)
        loop = True

#Sistem Register
if login == False :
    print(" ")
    print("="*50)
    print(" "*18,"MENU REGISTER")
    print("="*50)
    username_baru = str(input("Masukkan Username Baru Anda: "))
    password_baru = str(input("Masukkan Password Baru Anda: "))

    while username_baru in userpass :                   #Dictionary tidak diupdate ketika user menginput key yang sama
        print("="*50)
        print("Username sudah digunakan, MOHON masukkan username \nbaru")
        print("="*50)
        print(" ")
        print("="*50)
        print(" "*18,"MENU REGISTER")
        print("="*50)
        username_baru = str(input("Masukkan Username Baru Anda: "))
        password_baru = str(input("Masukkan Password Baru Anda: "))
    else :                                              #Dictionary diupdate ketika key belum digunakan
        userpass.update({username_baru:password_baru})
        print("="*50)
        print("Username dan Password BERHASIL terdaftar. Silahkan \nLogin")
        print("="*50)
    #print(f'Ini dictionary terbaru{userpass}')         #Digunakan untuk mengecek isi dictionary
    
    #Run Login setelah Register, Tanpa pilihan Login/Register
    print(" ")
    print("="*50)
    print(" "*18,"MENU LOGIN 2")
    print("="*50)
    username = str(input("Masukkan Username Anda: "))
    password = str(input("Masukkan Password Anda: "))

    if username in userpass and password == userpass[username] :
        nilai = True
    else :
        nilai = False

    while nilai == False :
        print("="*50)
        print("Anda Gagal Login, Mohon masukkan Username dan \nPassword yang benar")
        print("="*50)
        print(" ")
        print("="*50)
        print(" "*18,"MENU LOGIN 2")
        print("="*50)
        username = str(input("Masukkan Username Anda: "))
        password = str(input("Masukkan Password Anda: "))

        if username in userpass and password == userpass[username] :
            nilai = True
        else :
            nilai = False
    
#Sistem Login
elif login == True :
    print(" ")
    print("="*50)
    print(" "*18,"MENU LOGIN 1")
    print("="*50)
    username = str(input("Masukkan Username Anda: "))
    password = str(input("Masukkan Password Anda: "))

    if username in userpass and password == userpass[username] :
        nilai = True
    else :
        nilai = False

    while nilai == False :
        print("="*50)
        print("Anda Gagal Login, Mohon masukkan Username dan \nPassword yang benar")
        print("="*50)
        print(" ")

        #Sistem Pemilihan Login dan Register
        print("="*50)
        print(" "*7,"MENU PEMILIHAN LOGIN DAN REGISTER")
        print("="*50)
        print("Berikut merupakan menu login ICL MOTOGARAGE")
        print("Ketik 1. untuk Login")
        print("Ketik 2. untuk Register")
        relog = str(input("Masukkan pilihan anda: ")) 
        if relog == "1" :
            login = True
            loop = False
        elif relog == "2" :
            login = False
            loop = False
        else :
            print(" ")
            print("="*50)
            print(" "*1,"Input SALAH, Mohon Masukkan Pilihan Yang BENAR")
            print("="*50)
            loop = True

        #Sistem Looping Menu Pemilihan (in loop)
        while loop == True :
            print("="*50)
            print(" "*7,"MENU PEMILIHAN LOGIN DAN REGISTER")
            print("="*50)
            print("Berikut merupakan menu login ICL MOTOGARAGE")
            print("Ketik 1. untuk Login")
            print("Ketik 2. untuk Register")
            relog = str(input("Masukkan pilihan anda: ")) 
            if relog == "1" :
                login = True
                loop = False
            elif relog == "2" :
                login = False
                loop = False
            else :
                print(" ")
                print("="*50)
                print(" "*1,"Input SALAH, Mohon Masukkan Pilihan Yang BENAR")
                print("="*50)
                loop = True
        #Pemilihan (in Loop)
            if relog == "1" :
                login = True
                loop = False
            elif relog == "2" :
                login = False
                loop = False
            else :
                print(" ")
                print("="*50)
                print(" "*1,"Input SALAH, Mohon Masukkan Pilihan Yang BENAR")
                print("="*50)
                loop = True

        #Register (in Loop)
        if login == False :
            print(" ")
            print("="*50)
            print(" "*18,"MENU REGISTER")
            print("="*50)
            username_baru = str(input("Masukkan Username Baru Anda: "))
            password_baru = str(input("Masukkan Password Baru Anda: "))

            while username_baru in userpass :                   #Dictionary tidak diupdate ketika user menginput key yang sama
                print("="*50)
                print("Username sudah digunakan, MOHON masukkan username \nbaru")
                print("="*50)
                print(" ")
                print("="*50)
                print(" "*18,"MENU REGISTER")
                print("="*50)
                username_baru = str(input("Masukkan Username Baru Anda: "))
                password_baru = str(input("Masukkan Password Baru Anda: "))
            else :                                              #Dictionary diupdate ketika key belum digunakan
                userpass.update({username_baru:password_baru})
                print("="*50)
                print("Username dan Password BERHASIL terdaftar. \nSilahkan Login")
                print("="*50)
            #print(f'Ini dictionary terbaru{userpass}')         #Digunakan untuk mengecek isi dictionary
            
            #Run Login setelah Register, Tanpa pilihan Login/Register
            print(" ")
            print("="*50)
            print(" "*18,"MENU LOGIN 2")
            print("="*50)
            username = str(input("Masukkan Username Anda: "))
            password = str(input("Masukkan Password Anda: "))

            if username in userpass and password == userpass[username] :
                nilai = True
            else :
                nilai = False

            while nilai == False :
                print("="*50)
                print("Anda Gagal Login, Mohon masukkan Username dan \nPassword yang benar")
                print("="*50)
                print(" ")
                print("="*50)
                print(" "*18,"MENU LOGIN 2")
                print("="*50)
                username = str(input("Masukkan Username Anda: "))
                password = str(input("Masukkan Password Anda: "))
                
                if username in userpass and password == userpass[username] :
                    nilai = True
                else :
                    nilai = False
                        
        #Sistem Login (Loop)
        elif login == True :
            print(" ")
            print("="*50)
            print(" "*18,"MENU LOGIN 1")
            print("="*50)
            username = str(input("Masukkan Username Anda: "))
            password = str(input("Masukkan Password Anda: "))

            if username in userpass and password == userpass[username] :
                nilai = True
            else :
                nilai = False
                
#Tambahan Menu Pemilihan 2 (Perhitungan atau Update Polis Asuransi + Biaya Admin)
loopmenu = True
while loopmenu == True:
    menu_2 = update()
    #Perhitungan Suku Bunga dan Cicilan
    if menu_2 == "1" :
        perhitungan_biaya()
        loopmenu = False
    #Update Biaya   
    elif menu_2 =="2" :
        print(" ")
        print("="*50)
        print(" "*16,"UPDATE BIAYA")
        print("="*50)
        polis_asuransi = int(input("Masukkan Update Biaya Polis Asuransi: "))
        administrasi = int(input("Masukkan Update Biaya Administrasi: "))
        loopmenu = True

#Pertanyaan Perbandingan
n = 1
perbandingan = str(input("Apakah anda ingin melakukan perbandingan? \n(yes/no): ")).lower()

#Tambahan Menu Pemilihan 2 (Perhitungan atau Update Polis Asuransi + Biaya Admin)
while perbandingan == "yes":
    loopmenu = True
    while loopmenu == True:
        menu_2 = update()
        if menu_2 == "1" :
            perhitungan = True
        elif menu_2 =="2" :
            perhitungan = False

        #Fitur Perbandingan dijalankan 
        if perhitungan == True :
            print(" ")
            print("="*50)
            print(" "*1,"PERBANDINGAN SUKU BUNGA DAN CICILAN BULANAN",n)
            print("="*50)
            n += 1
            harga_mobil = int(input("Masukkan Harga Mobil\t\t: "))
            tenor = int(input("Masukkan Tenor(dalam bulan)\t: "))
            DP = float(input("Masukkan Down Payment\t\t: "))
            suku_bunga = float(input("Masukkan Suku Bunga\t\t: "))
            uang_muka = DP * harga_mobil

            #Plafon Pinjaman                
            plafon_pinjaman = int(harga_mobil - (uang_muka/100))

            #Angsuran Pokok Bulanan
            angsuran_pokok = int(plafon_pinjaman/tenor)

            #Angsuran Bunga Bulanan
            angsuran_bunga = int(plafon_pinjaman * suku_bunga/1200)

            #Total Cicilan Bulanan
            total_cicilan = angsuran_pokok + angsuran_bunga

            #Pembayaran Pertama Kali
            asuransi = 5/100 * harga_mobil
            provisi = 5/1000 * plafon_pinjaman
            pembayaran_pertama = int((uang_muka/100) + total_cicilan + asuransi + provisi + polis_asuransi + administrasi)

            #Output
            print(" ")
            print("="*50)
            print(" "*16,"HASIL PERHITUNGAN")
            print("="*50)
            print("Plafon Pinjaman\t\t: Rp",(plafon_pinjaman))
            print("Angsuran Pokok Perbulan\t: Rp",(angsuran_pokok))
            print("Angsuran Bunga Perbulan\t: Rp",(angsuran_bunga))
            print("Total Cicilan Perbulan\t: Rp",(total_cicilan))
            print("Pembayaran Pertama Kali\t: Rp",(pembayaran_pertama))
        
            #Penghentian Loop
            loopmenu = False
        elif perhitungan == False :
            print(" ")
            print("="*50)
            print(" "*16,"UPDATE BIAYA")
            print("="*50)
            polis_asuransi = int(input("Masukkan Update Biaya Polis Asuransi: "))
            administrasi = int(input("Masukkan Update Biaya Administrasi: "))
            loopmenu = True

    perbandingan = str(input("Apakah anda ingin melakukan perbandingan? \n(yes/no): ")).lower()
else :
    print(" ")
    print("="*50)
    print(" "*8,"TERIMA KASIH SUDAH BERTRANSAKSI")
    print("="*50)