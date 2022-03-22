class Hero:
    def __init__(self,name,health,attack,resistance):
        self.name = name
        self.health = health
        self.attack = attack
        self.resistance = resistance
    
    def serang(self,enemy):
        print(f"{self.name} menyerang {enemy.name}")
        enemy.diserang(self, self.attack)

    def diserang(self,enemy,attack):
        print(f"{self.name} diserang {enemy.name}")
        damage = attack - self.resistance
        print(f"Luka diterima : {str(damage)}")
        self.health -= damage
        print(f"darah {self.name} tersisa {str(self.health)}")

miya = Hero("Miya",100,20,5)
zilong = Hero("Zilong",150,15,8)

while True :
    miya.serang(zilong)
    print(" ")
    zilong.serang(miya)
    print(" ")
    if zilong.health <= 0 :
        print("=== Zilong Dead ===")
        break
    elif miya.health <= 0 :
        print("=== Miya Dead ===")
        break

