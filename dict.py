import pandas as pd


dataa = []
data1 = {'nama': 'vio', 'usia': 12, 'makanan': 'ayam'}
data2 = {'nama': 'niko', 'usia': 13, 'makanan': 'sapi'}
dataa.append(data1)
dataa.append(data2)
print(dataa)
dataa = pd.DataFrame(dataa)
print(dataa)
dataa['usia_awal'] = dataa['usia']
dataa['usia_akhir'] = dataa['usia']
dataa['makanan_awal'] = dataa['makanan']
dataa['makanan_akhir'] = dataa['makanan']
print(dataa)
print()

datab = []
datab.append({'nama': 'gbay', 'usia': 14, 'makanan': 'entah'})
datab.append({'nama': 'maria', 'usia': 15, 'makanan': 'ayam?'})
print(datab)
datab = pd.DataFrame(datab)
print(datab)
datab['usia_awal'] = datab['usia']
datab['usia_akhir'] = datab['usia']
datab['makanan_awal'] = datab['makanan']
datab['makanan_akhir'] = datab['makanan']
print(datab)
print()

datac = [
    {'nama': 'vio', 'usia': 12, 'makanan': 'ayam'},
    {'nama': 'niko', 'usia': 13, 'makanan': 'sapi'},
    {'nama': 'gbay', 'usia': 14, 'makanan': 'entah'},
    {'nama': 'maria', 'usia': 15, 'makanan': 'ayam?'}
]
print(datac)
datac = pd.DataFrame(datac)
print(datac)

datac['usia_awal'] = datac['usia']
datac['usia_akhir'] = datac['usia']
datac['makanan_awal'] = datac['makanan']
datac['makanan_akhir'] = datac['makanan']
print(datac)