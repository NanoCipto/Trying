a = "ICL"
myvar = "ICL"
my_var = "ICL"
MyVar = "ICL"
b = "Hello World"



print (myvar)
print (b)

#Yang tidak boleh dilakukan


a = "dosen icl"
b = 2020

print (a)
print (b)

#Penulisan yang salah
'''a = dosen aukdk -> tanpa petik 2
b = "2020" -> dengan petik 2'''


a = "ICL"
print (a)
#yang di print adalah a yang dideklarasikan di atasnya
a = "Dosen ICL"
print (a)
#yang di print adalah a yang dideklarasikan di atasnya

#Penggunaan Number
'''Penggunaan Integer'''
myint = 7           
print (myint)

'''Penggunaan Float'''
myfloat = 7.0       
print (myfloat)

myfloat = float (7)
print (myfloat)

#Penggunaan String
mystring = 'hello'
print (mystring)

mystring = "hello"
print (mystring)

mystring = "Don't Worry about apostrophes"
print (mystring)
'''Penggunaan string menggunakan apostrophes atau tanda petik dua'''

#Creation
word = "Hello World"
print (word)

#Accessing
word = "Hello World"
letter = word[0]  #Indeks ke 0
print (letter)
#Finding
word = "Hello World"
print (word.count ('l')) #Menghitung banyaknya I dalam string

print (word.find ("H")) # menemukan huruf H dalam string

print (word.index ("World")) #menemukan huruf dalam kata-kata tersebut

#Count
s = "Count, the number of spaces"
print (s.count (''))

#Split Strings
word = "Hello World"
print (word.split ('Hello World'))  #Split on whitespaces

#Length
word = "Hello World"
print (len(word))

#Startswith/Endwith
word = "Hello World"
print (word.startswith ("H"))

print (word.endswith("d"))

print (word.endswith("W"))

#Slicing
'''Use[#:#]'''
word = ("Hello World")
print (word [0])
print (word [0:1])
print (word [0:3])
print (word [:3])
print (word [-3:])
print (word [3:])
print (word [:-3])

#Changing Upper and Lower Caswe Strings
string = "Hello World"
print (string.upper())
print (string.lower())
print (string.title())
print (string.capitalize())

#Concatenation

#Join
word = "Hello World"
print (":".join (word))

#Repeat Strings
print ("."*10)

#Replacing
word = "Hello World"
print (word.replace ("Hello", "Goodbye"))

#Simple Operators can be executed on numbers

#Deklarasi bisa dilakukan dalam satu baris
a,b = 3,4
print (a,b)
'''Tetapi tidak bisa menggabungkan angka dan kata'''

#List
daftar = ['satu', 'dua', 'tiga', 'empat']
daftarkecil = ['satu', 'dua']
daftar.extend (daftarkecil)
print (daftar)
'''List, data di dalam tabel bisa ditambahkan, diubah dan dihapus
Untuk memanggil data, yaitu dengan cara memanggil nomor indeksnya'''
#Update Item in a List
z = [3, 7, 4, 2]
z[1]="fish"
print (z)

#Count Method
random_list = [4,1,5,4,10,4]
random_list.count (5)
print (random_list.count(5))

#Sort Method
z = [3, 7, 4, 2]
z.sort ()
print (z) #Mengurutkan dan harus mempunyai tipe yang sama

#Append Method (Additional/Penambahan)
z = [3, 7, 4, 2]
z.append (3)
print (z)

#Remove Method
z = [3, 7, 4, 2]
z.remove (2)
print (z)

#Pop Method
z = [3, 7, 4, 2]
z.pop (1)
print (z)

#Extend Method
z = [3, 7, 4, 2]
z.extend ([4,5])
print (z)

#Insert Method
z = [3, 7, 4, 2, 1]
z.insert (4,[1,2])
print (z) #Kurung kotak bisa dihilangkan menggunakan flattern

#Tuple
'''memiliki indeks, sama seperti list tetapi tidak bisa dimanipulasi'''

#Dictionary
daftar= {'nama':'nova', "Laboratorium": 'ICL', 'Angkatan': 2021}
print (daftar)
'''bisa diotak-atik. Jika ingin memanggil value, maka harus memanggil key-nya'''
#Set
merk_mobil = {"panther", "Kijang", "Komodo"}
print (merk_mobil)
'''Tidak memiiliki indeks, dan data yang sama akan tereliminasi'''
#Type Conversion
'''int()
float ()
dst'''