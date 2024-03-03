import pandas as pd


class DataProcessor:
    def __init__(self, data):
        self.data = data

    def preprocess(self):
        # Contoh metode untuk melakukan pra-pemrosesan data
        # Misalnya, normalisasi data atau penghapusan outlier
        pass

    def analyze(self):
        # Contoh metode untuk melakukan analisis data
        # Misalnya, menghitung rata-rata, median, atau visualisasi data
        pass

# Contoh penggunaan kelas DataProcessor
data = [10, 20, 30, 40, 50]
processor = DataProcessor(data)
processor.preprocess()
processor.analyze()


