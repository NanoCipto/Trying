username_fix = "abcd"
password_fix = 1234

username = input("Masukkan username: ")
password = int(input("Masukkan password: "))

while username_fix != username :
    print("Username atau Password Salah")
    username = input("Masukkan username: ")
    password = int(input("Masukkan password: "))
else :
    pass
while password_fix != password :
    print("Username atau Password Salah")
    username = input("Masukkan username: ")
    password = int(input("Masukkan password: "))
else :
    pass

print("Login Anda Berhasil")