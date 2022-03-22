#Deklarasi Variabel
polis_asuransi = 40000
administrasi = 700000
userpass = {"admin":"1234"}

def login():
    print("="*50)
    print(" "*7,"MENU PEMILIHAN LOGIN DAN REGISTER")
    print("="*50)
    print("Berikut adalah menu login ICL MOTOGARAGE")
    print("Tekan 1. untuk login")
    print("Tekan 2. untuk register akun")
    return input("Masukan pilihan anda : ")

def menu():
    #Sistem Menu Pemilihan
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
def update() :
    print(" ")
    print("="*50)
    print(" "*16,"UPDATE BIAYA")
    print("="*50)

#Sistem Menu Pemilihan
relog = login()
while True:
    #Sistem Login
    if relog == "1":
        print(" ")
        print("="*50)
        print(" "*18,"MENU LOGIN")
        print("="*50)
        username = input("Masukkan username anda : ")
        password = input("Masukan Password anda : ")
        if username in userpass and password == userpass[username]:
            print("Login BERHASIL")
            break                                     #Ini Untuk Keluar dari Looping
        else:
            print("Anda Gagal Login, Mohon masukkan Username dan \nPassword yang benar")
            relog = login()
    #Sistem Register
    elif relog =="2":
        print(" ")
        print("="*50)
        print(" "*18,"MENU REGISTER")
        print("="*50)
        username_baru = input("masukkan username baru : ")
        while username_baru in userpass:
            print("Username sudah digunakan, MOHON masukkan username \nbaru")
            username_baru = input("Masukkan username baru : ")
        password_baru = input("Masukkan Password Anda : ")
        userpass.update({username_baru:password_baru})
        print("Username dan Password BERHASIL terdaftar. \nSilahkan Login")
        relog = login()

#Menu Utama
main_menu = menu()
while True :
    #Sistem Perhitungan
    if main_menu == "1" :
        perhitungan_biaya()
        break
    #Sistem Update Polis Asuransi dan Administrasi
    elif main_menu == "2" :
        update()
        polis_asuransi = int(input("Masukkan Update Biaya Polis Asuransi: "))
        administrasi = int(input("Masukkan Update Biaya Administrasi: "))
        main_menu = menu()

perbandingan = str(input("Apakah anda ingin melakukan perbandingan? \n(yes/no): ")).lower()
while perbandingan == "yes":
    while True :
        main_menu = menu()
        #Sistem Perhitungan
        if main_menu == "1" :
            perhitungan_biaya()
            perbandingan = str(input("Apakah anda ingin melakukan perbandingan? \n(yes/no): ")).lower()
            break
        #Sistem Update Polis Asuransi dan Administrasi
        elif main_menu == "2" :
            update()
            polis_asuransi = int(input("Masukkan Update Biaya Polis Asuransi: "))
            administrasi = int(input("Masukkan Update Biaya Administrasi: "))
            main_menu = menu()

print(" ")
print("="*50)
print(" "*8,"TERIMA KASIH SUDAH BERTRANSAKSI")
print("="*50)