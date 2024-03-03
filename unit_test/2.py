import pandas as pd
import unittest

def tambah_kolom(df):
    # Menambahkan kolom baru 'nilai_total' yang merupakan jumlah dari kolom 'nilai1' dan 'nilai2'
    df['nilai_total'] = df['nilai1'] + df['nilai2']
    return df

class TestDataFrameMethods(unittest.TestCase):
    # Test case untuk memastikan fungsi tambah_kolom berperilaku dengan benar
    
    def test_tambah_kolom(self):
        # Membuat DataFrame contoh untuk diuji
        data = {'nama': ['A', 'B', 'C'],
                'nilai1': [80, 90, 85],
                'nilai2': [70, 85, 80]}
        df = pd.DataFrame(data)
        
        # Memanggil fungsi tambah_kolom untuk menguji
        # df['nilai_total'] = df['nilai1'] + df['nilai2']
        # df_hasil = df
        df_hasil = tambah_kolom(df)

        
        # Memeriksa apakah kolom 'nilai_total' telah ditambahkan dengan benar
        self.assertTrue('nilai_total' in df_hasil.columns)
        
        # Memeriksa apakah hasil penambahan kolom sesuai dengan yang diharapkan
        self.assertListEqual(list(df['nilai_total']), [150, 175, 165])

if __name__ == '__main__':
    # Menjalankan pengujian
    unittest.main()
