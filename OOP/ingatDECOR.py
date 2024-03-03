import pandas as pd
import time

def decor(func):
    def wrap():
        print('sebelum')
        func()
        print('sesudah')
        print()
    return wrap

@decor
def makan():
    print('nasi goreng')
makan()



def decor(func):
    def wrap(x):
        print('sebelum')
        func(x)
        print('sesudah')
        print()
    return wrap

@decor
def minum(x):
    print(f'saya suka {x}')
minum('jus')


def timer(func):
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()  # Catat waktu mulai
            result = func(*args, **kwargs)  # Jalankan fungsi
            end_time = time.time()  # Catat waktu selesai
            print(f"Elapsed time: {end_time - start_time} seconds")  # Cetak waktu yang dibutuhkan
            return result
        except Exception as e:
            print(f"Error occurred: {e}")  # Cetak pesan kesalahan
    return wrapper

@timer
def process_dataframe(x):
    x['new_column'] = x['old_column'] * 2
    return x

data = {'old_column': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

print(process_dataframe(df.copy()))


class Mobil:
    def __init__(self, merek):
        self.merek = merek
    @staticmethod
    def intro(x):
        print(f"Ini adalah awal mobil {x}")
        
    @staticmethod
    def outro(x):
        print(f"Ini adalah awal mobil {x}")
        
    def outro2(self):
        print(f"Ini adalah awal mobil {self.merek}")

Mobil.intro('bmw')
mobil = Mobil('bmw')
print(mobil.merek)
mobil.intro(mobil.merek)
mobil.outro('bmw')
mobil.outro2()
print()



class Mobil:
    def __init__(self, merek):
        self.merek = merek
    @classmethod
    def intro(cls, x):
        print(f"Ini adalah awal mobil {x}, {cls}")
    
    @classmethod   
    def outro(x, merk):
        print(f"Ini adalah awal mobil {merk}, {x}")
    
    def outro2(self):
        print(f"Ini adalah awal mobil {self.merek}")

Mobil.intro('mercedez')
mobil1 = Mobil('mercedez')
Mobil.intro(mobil1.merek)
print(mobil1.merek)
mobil1.outro(mobil1.merek)
mobil1.outro2()