import requests
import pandas as pd

url = "https://ipinfo.io/161.185.160.93/geo"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    df = pd.DataFrame({
        'Data IP':data
        })
    print(df)
else:
    print("Failed to retrieve data:", response.status_code)