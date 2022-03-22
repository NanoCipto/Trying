'''Membuat Kelas (Class Variable)'''
class data_civitas:
    name = None
    program_studi = None

#Membuat Objek
andi = data_civitas()
andi.name = "Andi"
andi.program_studi = "Teknik Industri"
print(andi.name)
print(andi.program_studi)

budi = data_civitas()
budi.name = "Budi"
budi.program_studi = "Teknik Kimia"
print(budi.name)
print(budi.program_studi)

'''Membuat Atribut Objek Class'''
class data_civitas2():
    jumlah_civitas = 0
    def __init__(self,name,programstudi):
        self.name = name
        self.prodi = programstudi
        self.status = "Aktif"
        data_civitas2.jumlah_civitas +=1                #Untuk Mengetahui seberapa banyak objek yang kita buat

#Membuat Objek
wahono = data_civitas2("Wahono","TI")
print(wahono.name)
print(wahono.prodi)
print(wahono.status)
print(data_civitas2.jumlah_civitas)

ojan = data_civitas2("Fauzan","TI")
print(ojan.name)
print(ojan.prodi)
print(ojan.status)
print(data_civitas2.jumlah_civitas)

'''Membuat Method dari Objek'''
class data_civitas3():
    jumlah_civitas = 0
    def __init__(self,name,programstudi):
        self.name = name
        self.prodi = programstudi
        self.status = "Aktif"
        data_civitas3.jumlah_civitas +=1                #Untuk Mengetahui seberapa banyak objek yang kita buat
    def keterangan(self):
        return f"Hallo nama saya {self.name} dan saya ada di prodi {self.prodi}"

#Membuat Objek
wahono = data_civitas3("Wahono","Teknik Industri 21")
print(wahono.keterangan())

yoga = data_civitas3("Yoga","Teknik Industri 21")
print(yoga.keterangan())

'''Inheritance/Pewarisan'''
class data_civitas4():
    jumlah_civitas = 0
    def __init__(self,name,programstudi):
        self.name = name
        self.prodi = programstudi
        self.status = "Aktif"
        data_civitas4.jumlah_civitas +=1                #Untuk Mengetahui seberapa banyak objek yang kita buat
    def keterangan(self):
        return f"Hallo nama saya {self.name} dan saya ada di prodi {self.prodi}"

class data_mahasiswa(data_civitas4):
    jumlah_mahasiswa = 0
    def __init__(self,name,prodi,nim,semester):
#       self.nama = nama            Tidak Efektif
#       self.prodi = prodi          Tidak Efektif
        super().__init__(name,prodi)        #Menjalankan Fungsi dari line 62 - 66
        self.nim = nim
        self.semester = semester
        data_mahasiswa.jumlah_mahasiswa +=1
    
#Membuat Objek
wahono = data_mahasiswa("Wahono","Teknik Industri","2150","4")

print(wahono.name)
print(wahono.keterangan())

'''Override : Penimpaan/Replacement'''
class data_civitas5():
    jumlah_civitas = 0
    def __init__(self,name,programstudi):
        self.name = name
        self.prodi = programstudi
        self.status = "Aktif"
        data_civitas5.jumlah_civitas +=1                #Untuk Mengetahui seberapa banyak objek yang kita buat
    def keterangan(self):
        return f"Hallo nama saya {self.name} dan saya ada di prodi {self.prodi} dan saya adalah civitas"

class data_mahasiswa(data_civitas5):
    jumlah_mahasiswa = 0
    def __init__(self,name,prodi,nim,semester):
        super().__init__(name,prodi)        #Menjalankan Fungsi dari line 62 - 66
        self.nim = nim
        self.semester = semester
        data_mahasiswa.jumlah_mahasiswa +=1
    def keterangan(self):           #Method Child Menimpa Parent (Override)
        return f"Hallo nama saya {self.name} dan saya ada di prodi {self.prodi}, nim saya {self.nim} dan saya adalah mahasiswa"

class data_dosen(data_civitas5):
    jumlah_dosen = 0
    def __init__(self, nama, prodi,nip,matkul):
        data_civitas5.__init__(self,nama,prodi)
        self.nip = nip
        self.matkul = matkul
        data_dosen.jumlah_dosen +=1
    def keterangan(self):           
        return f"Hallo nama saya {self.name} dan saya ada di prodi {self.prodi}, nip saya {self.nip} dan saya adalah dosen {self.matkul}"

#Membuat Objek
wahono = data_mahasiswa("Wahono","Ti","2150",4)
ojan = data_mahasiswa("Fauzan","Ti","2150",4)
yoga = data_mahasiswa("Yoga","Ti","2150",4)
budi = data_civitas5("Budi","Industri")
ahmad = data_dosen("Ahmad","TI","1970","Statistika")
arief = data_dosen("Arief","Industri","1999","Alprog")

print(wahono.keterangan())
print(budi.keterangan())
print(ahmad.keterangan())

print("Jumlah mahasiswa: ",data_mahasiswa.jumlah_mahasiswa)
print("Jumlah Dosen: ",data_dosen.jumlah_dosen)
print("Jumlah Civitas: ",data_civitas5.jumlah_civitas)

import imp
from matplotlib import pyplot
import numpy as np
array1 = np.array([1,2,3,4,5,6])
array2 = np.arange(1,7,1)
arraymd = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
print(array1)
print(array2)
print(arraymd)

#Merubah bentuk dari matriks
bentuk1 = array1.reshape(2,3)
print(bentuk1)

#Untuk Mengetahui Bentuk dan Jumlah Item pada Array

print(arraymd.shape)
print(arraymd.size)

#Membuat matriks nol,satu,identitas
matriksnol = np.zeros([5,5])
print(matriksnol)
matrikssatu = np.ones([5,5])
print(matrikssatu)
matriksidentitas = np.eye(5)
print(matriksidentitas)

import pandas as pd
#Membuat Series
series1 = pd.Series(array1)
print(series1)
series2 = pd.Series(array2,["Satu","Dua","Tiga","Empat","Lima","Enam"])
print(series2)
#Membuat DataFrame
dataframe1 = pd.DataFrame([array1,array2],["Indeks 1","Indeks 2"],["Satu","Dua","Tiga","Empat","Lima","Enam"])
print(dataframe1)
tabel2 ={
    "Array1" : array1,
    "Array2" : array2,
}
dataframe2 = pd.DataFrame(tabel2,["Satu","Dua","Tiga","Empat","Lima","Enam"])
print(dataframe2)

#Matplotlib
import matplotlib.pyplot as plt
x = ["Jumlah Civitas","Jumlah Dosen","Jumlah Mahasiswa"]
y = [data_civitas5.jumlah_civitas,data_dosen.jumlah_dosen,data_mahasiswa.jumlah_mahasiswa]
plt.title("Grafik Data Civitas")

#plt.bar(x,y)
plt.pie(y)
#plt.hist(y)
plt.show()