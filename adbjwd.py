class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print(f"Perkenalkan nama saya{self.nama} dari {self.asal}")

class Pelajar(Orang):
    def __init__(self, nama, asal, sekolah):
        super().__init__(nama,asal)
        self.sekolah = sekolah
    
    def perkenalan(self):
        print(f"Asal sekolah saya dari{self.sekolah}")

addis = Pelajar("Addis","Sidoarjo","SMA MANA AJA")
addis.perkenalan()