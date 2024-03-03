import pandas as pd
import time

# Definisikan dekorator
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Catat waktu mulai
        result = func(*args, **kwargs)  # Jalankan fungsi
        end_time = time.time()  # Catat waktu selesai
        print(f"Elapsed time: {end_time - start_time} seconds")  # Cetak waktu yang dibutuhkan
        return result
    return wrapper

# Contoh fungsi untuk memanipulasi DataFrame
@timer
def process_dataframe(x):
    # Contoh manipulasi DataFrame
    x['new_column'] = x['old_column'] * 2
    return x

# Buat DataFrame contoh
data = {'old_column': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

@timer
def process_dataframe2(x):
    x['Newest_column'] = x['new_column']*3
    return x


# Panggil fungsi yang telah didekorasi
result_df = process_dataframe(df.copy())
print(result_df)

last = process_dataframe2(result_df)
print(last)

print(df)
print(result_df)