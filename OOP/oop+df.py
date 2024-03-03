import pandas as pd

class Proses:
    def __init__(self, df):
        self.dataframe = df

    def tambah(self):
        self.dataframe['new_column'] = self.dataframe['old_column'] * 2
        return self.dataframe
        
    def tambah2(self):
        self.dataframe['newest_column'] = self.dataframe['new_column'] * 3
        return self.dataframe
data = {'old_column': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
print(df)

prosesor = Proses(df)


hasil = prosesor.tambah()
print(hasil)

hasil = Proses(hasil)
hasil_akhir = hasil.tambah2()
print(hasil_akhir)