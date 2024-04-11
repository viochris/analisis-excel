import requests
import pandas as pd

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)

# print(response.json())

# Memeriksa apakah respons berhasil
if response.status_code == 200:
    data = response.json()
    # Sekarang 'data' berisi informasi properti dalam format JSON
    # Anda dapat menganalisisnya sesuai kebutuhan Anda
    # print(data)
    
    df = pd.DataFrame(data['bpi'])
    # print(df)
    df = df.T
    print(df)
    
    for key, items in data['time'].items():
        print(items)
    

else:
    print("Failed to retrieve data:", response.status_code)
    
