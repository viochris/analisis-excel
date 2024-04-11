import requests
import pandas as pd

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    df = pd.DataFrame({
        'USD': data['bpi']['USD'],
        'GBP': data['bpi']['GBP'],
        'EUR': data['bpi']['EUR']
    })
    print(df)
    
    
    for key, items in data['time'].items():
        print('Type: ', key, ',   ', 'Time: ', items)
    
    
else:
    print("Failed to retrieve data:", response.status_code)