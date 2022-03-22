# Wahono Hadi Sucipto
# 215060700111004
# Kelas F

x = 12
y = 4

#Arithmetic Operators
print (x + y)
print (x - y)
print (x * y)
print (x / y)
print (x % y)
print (x**y)
print (x//y)

#Assignment Operators
x = 12
y = 4

x = x + 4      #Deklarasi x baru
print (x)
y += 2
print (y)

x = 12
y = 4

x *= 5
print (x)
print (x,y)

#Unary Operator
n = 9
print (n)
n = -n
print (n)

#Relational Operators
print (x < y)
print (x > y)
print (x == y)

x = 4
print (x == y)
print (x <= y)
print (x >= y)
print ( x != y)

#Logical Operators
x = 12
y = 4
print (x < 20 and y < 5)
print (x > 20 and y < 5)
print (x > 20 and y > 5)
print (x < 20 or y < 5)
print (x > 20 or y < 5)
print (x > 20 or y > 5)
print (not x < 20 or not y < 5)
print (not x > 20 or y < 5)
print (not x > 20 or y > 5)
    #perintah not berlaku pada satu fungsi tepat dibelakangnya
    #perintah not tidak berlaku pada or ataupun and

#Membuat Perintah Sederhana Sendiri
n = 3
while n > 1:
     print ("Mohon Maaf Apabila Saya Pernah Melakukan Kesalahan Bu")
     n = n - 1
else : print ("Semoga UTSnya Dimudahkan Aamiin")
n = n - 1

a = 20
while a >= 1:
     print ("Terima Kasih Bu Widha")
     a = a - 1

#Membuat Kalkulator Sederhana
def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y

print("Pilih Operasi.")
print("a.Jumlah")
print("b.Kurang")
print("c.Kali")
print("d.Bagi")

choice = input("Masukkan pilihan(a/b/c/d): ")
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
if choice == 'a':
   print(a,"+",b,"=", add(a,b))
elif choice == 'b':
   print(a,"-",b,"=", subtract(a,b))
elif choice == 'c':
   print(a,"*",b,"=", multiply(a,b))
elif choice == 'd':
   print(a,"/",b,"=", divide(a,b))
else:
   print("Aduh Aku Pusying")