class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i
    def tambah(self, _i): 
        return self.i + _i
    def kurang(self, _i):
        return self.i - _i

hitung = Kalkulator(10)
print(hitung.tambah(5))
print(hitung.kurang(5))
    
