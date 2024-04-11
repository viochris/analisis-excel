import requests
import pandas as pd

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    

    df = pd.DataFrame(data['bpi']).T
    print(df)
    
    df = pd.DataFrame.from_dict(data['bpi'], orient='index')
    print(df)
    
    df = pd.DataFrame({'waktu':data['time']})
    print(df)
    
    
    for key, items in data['time'].items():
        print('Type: ', key, ',   ', 'Time: ', items)
    
    
else:
    print("Failed to retrieve data:", response.status_code)