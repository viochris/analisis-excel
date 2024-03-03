import pandas as pd
import pickle

data = {'text': ['apple', 'banana', 'orange', 'dragonfruit']}
df = pd.DataFrame(data)

# menyimpan
contoh_dictionary = df
pickle_keluar = open("df.pickle","wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()

# akses
pickle_masuk = open("df.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()
print(contohDictionary)