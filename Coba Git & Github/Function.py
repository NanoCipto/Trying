'''Fungsi Sederhana'''
def halo_dunia():
    print("Halo python! Halo dunia!")

halo_dunia()
halo_dunia()
halo_dunia()
halo_dunia()

'''Fungsi dengan Argumen atau Parameter'''
def selamat_datang(nama):
    print(f"Halo {nama}, selamat datang!")
    print("Hallo",nama,"selamat datang!")
    print("Hallo {}, selamat datang!",format(nama))

selamat_datang("Nurul")
selamat_datang("Lendis")
selamat_datang("Fabri")
selamat_datang("isa")

'''Parameter Wajib'''
def perkenalan (nama,asal):
    print(f"Perkenalkan saya {nama} dari {asal}")

perkenalan("Renza Ilhami", "Jawa Timur")

'''Parameter Opsional (atau Default)'''
def suhu_udara(daerah, derajat, satuan = "Celcius" ):
    print("Suhu di {daerah} adalah {derajat} {satuan}")

suhu_udara("Surabaya", "30")

'''Fungsi Dengan Parameter Tidak Seurut'''    
def suhu_udara(daerah, derajat = 30, satuan = "Celcius" ):
    print("Suhu di {daerah} adalah {derajat} {satuan}")

suhu_udara("Jakarta", satuan = "Fahrenheit")
suhu_udara(satuan = "Kelvin", daerah = "Makassar", derajat = 100)

'''Fungsi yang Mengembalikan Nilai'''
def luas_persegi (sisi):
    return sisi * sisi

print(f"Luas persegi dengan sisi 4 adalah", luas_persegi(4) )

'''Lebih dari 1 return'''
def persentase (total,jumlah):
    if (total >= 0 and total <= jumlah):
        return total/jumlah *100
    return False

print(persentase(30,60))
print(persentase(100,60))

'''Variabel Lokal dan Global'''
kota = "Lamongan"
def tempat():
    kota = "Surabaya"
    print(kota)

tempat()            #Variabel Lokal
print(kota)         #Variabel Global

'''Fungsi Rekursif'''
def halo_dunia():
    print("Halo Dunia!")
    #panggil dirinya sendiri
    halo_dunia()    #<-- rekursifitas

halo_dunia()

def tampilkan_angka(batas, i = 1):
    print(f"Perulangan ke {i}")

    if (i< batas):
        #Disini terjadi rekursifitas
        tampilkan_angka(batas, i + 1)

tampilkan_angka(10)