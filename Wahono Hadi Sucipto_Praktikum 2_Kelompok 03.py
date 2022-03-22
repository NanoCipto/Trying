# input  : Nama, Username, Password, Nama Kamar, Fasilitas, Harga, Charge,Tanggal Check-in, Lama Menginap 
# output : Detail Pemesanan Kamar
import datetime as dt
listkamar= [
           {
               "namakamar":"Reguler",
               "fasilitas":"\n 1. AC\n 2. Air Panas\n 3. Pembuat Kopi",
               "harga":"100000",
           },
           {
               "namakamar":"Golden",
               "fasilitas":"\n 1. AC\n 2. Air Panas\n 3. Pembuat Kopi\n 4. Balkon",
               "harga":"200000",
           },
           {
               "namakamar":"Platinum",
               "fasilitas":"\n 1. AC\n 2. Air Panas\n 3. Pembuat Kopi\n 4. Bath tub",
               "harga":"350000",
           },
           {
               "namakamar":"Presidental Suites",
               "fasilitas":"\n 1. AC\n 2. Air Panas\n 3. Pembuat Kopi\n 4. Balkon\n 5. Bath tub",
               "harga":"800000",
           }
]
charge =[
          {"Makan" : 100000},
          {"Sauna" : 150000},
          {"Salon" : 125000},
          {"Pijat" : 150000}
]
chargeterpilih={}

#login
userpass = {"admin":"123"}
userid = input("Masukkan Username: ")
password = input("Masukkan Password: ")
nama = input("Nama Pelangan\t: ")

if userid in userpass and password == userpass[userid] :
    print ("Login Berhasil")
else :
    print("Login Gagal")

#Halaman Utama
print("="*50)
print("Selamat datang di Hotel ICL")
print("="*50)

#Daftar Kamar
i = 0                                                           # i digunakan untuk menentukan penampilan indeks dari list kamar (line 53 - 55)
for indeks,item in enumerate(listkamar,start = 1) :             #start = 1, karena digunakan sebagai penomoran dan dimulai dari angka satu
    namakamar = listkamar[i]["namakamar"]                       #enumerate digunakan untuk penomoran list, dictionary dsb
    fasilitas = listkamar[i]["fasilitas"]                       #format penulisan = namalist[indeks list][key dari dictionary]
    harga = listkamar[i]["harga"]                               #(line 52) indeks,item adalah variabel bebas. Variabel ini wajib ada jika ingin mengakses list
    print(indeks,"Nama kamar : ",namakamar,"\nFasilitas: ",fasilitas,"\nHarga: ",harga, "\n")
    i+=1                                                        #i digunakan untuk memanggil indeks dari list yang isinya dictionary
    indeks+=1                                                   #indeks digunakan untuk penomoran
    #\n digunakan untuk enter otomatis dan harus berupa string

#Pemilihan Kamar
pilihan = int(input("Masukkan kode kamar pilihan: "))
kamarterpilih = listkamar[pilihan-1]["namakamar"]
print("Kamar yang anda pilih",kamarterpilih)
harga = listkamar[pilihan-1]["harga"]

#Daftar Charge yang Ada
print("Berikut adalah charge yang tersedia di Hotel ICL: ")
for i,item in enumerate(charge,start = 1) :
    for key,value in item.items() :
        print(i,key,":",value)
    i+=1

#Pilihan Charge
q = str(input("Apakah anda mau memilih charge? (yes/no): ")).lower()
while q == "yes" :
    pilihan2 = int(input("Pilihan Charge: "))
    for key,value in charge[pilihan2-1].items() :
        if key in chargeterpilih :
            print ("Anda telah memilih charge tersebut")
        chargeterpilih[key] = value
    q = input("Apakah anda ingin memilih charge lagi? (yes/no): ").lower()

#Tanggal dan Lama Menginap
checkIn = input("Masukkan tanggal check in (yyyy-mm-dd): ")
tanggalcheckIn = dt.datetime.strptime(checkIn, "%Y-%m-%d")
menginap = int(input("Lama menginap (hari): "))
tanggalcheckOut = tanggalcheckIn + dt.timedelta(menginap)
biayakamar = int(harga) * menginap

#Detail Pemesanan Kamar
print("="*50)
print(" "*12,"Detail Pesanan Kamar")
print("="*50)
print("Nama Pelanggan\t\t: ",nama)
print("Pilihan kamar\t\t: ",kamarterpilih) 
print("Lama menginap\t\t: ",menginap)
print("Tanggal Check In\t: ",tanggalcheckIn.date())
print("Tanggal Check Out\t: ", tanggalcheckOut.date())
if len(chargeterpilih) > 0 :
    print("Charge\t\t\t: ")
    for key,value in chargeterpilih.items() :
        print(key,"\t\t\t: ",value)
    print("Sub total Charge\t: ",sum(chargeterpilih.values())) 
print("Sub Total Biaya Kamar\t: ", biayakamar)
print("Grand Total\t\t: ",biayakamar + sum(chargeterpilih.values()))
print("="*50)

#\t digunakan untuk memberikan tab dan harus di dalam string