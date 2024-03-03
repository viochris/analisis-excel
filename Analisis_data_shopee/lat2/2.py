import pandas as pd

data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male'],
    'Brand': ['iPhone', 'Samsung', 'Samsung', 'iPhone', 'Samsung', 'iPhone', 'Samsung', 'iPhone', 'Samsung', 'iPhone', 'Sony', 'Huawei', 'Sony', 'Huawei', 'Sony', 'Huawei', 'Sony', 'Huawei', 'Sony', 'Huawei'],
}


df = pd.DataFrame(data)
# df = df[df['Brand'].str.lower().str.startswith(('s', 'i'))]
print(df)
hasil = df[df['Brand'].str.lower().isin(['samsung', 'iphone'])]
hasil = hasil.groupby(['Gender', 'Brand'])['Brand'].count().reset_index(name='Jumlah')
print(hasil)

hasil1 = df[df['Brand'] == 'Samsung']
hasil1 = hasil1.groupby('Gender')['Gender'].count()
print(hasil1)