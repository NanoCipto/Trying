userpass = {"kelompok3":"gg"}

def login():
  print("Berikut adalah menu login ICL MOTOGARAGE")
  print("Tekan 1. untuk login")
  print("Tekan 2. untuk register akun")
  return input("Masukan pilihan anda : ")

varlog = login()
while True: #ini terserah si kondisinya kek gimana bisa kalian pakein misal deklarasi dulu kaya punya kalian diatas login=True atau langsung True gini juga sama
  if varlog == "1":
    print("ini buat menu login")
    id = input("Masukkan username anda : ")
    pw = input("Masukan Password anda : ")
    if id in userpass and pw == userpass[id]:
      print("Login Sukses")
      break
    else:
      print("username / password salah")
      varlog = login()
  elif varlog =="2":
    print("ini buat menu register")
    newid = input("masukkan username baru : ")
    while newid in userpass:
      print("Username tsb sudah terdaftar")
      newid = input("Masukkan username baru : ")
    newpw = input("Masukkan Password Anda : ")
    userpass[newid] = newpw
    print("Selamat terdaftar")
    varlog = login()

print("ini dah keluar dari looping")
print("bisa di jadiin referensi buat perloginan")