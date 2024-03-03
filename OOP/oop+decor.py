class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil(x):
        print(f"Ini adalah awal mobil {x}")
        
    @staticmethod
    def outro_mobil(x):
        print(f"Ini adalah akhir mobil {x}")

    @staticmethod
    def check(*x):
        print(x)
    
Mobil.intro_mobil('bmw')
mobil_1 = Mobil("DicodingCar")
print(mobil_1.merek)
mobil_1.outro_mobil('bmw')
Mobil.check()
mobil_1.check()







class Mobil:
    def __init__(self, merek):
        self.merek = merek
    @classmethod
    def intro_mobil(cls, x):
        print(f"Ini adalah metode dari kelas Mobil {x}, ini {cls} ") 
Mobil.intro_mobil('bmx')
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil('mbw')


# nama tidak harus intro_mobil(cls)
class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(args, nama):
        print(args, nama)
Mobil.intro_mobil('vio')
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil('v')