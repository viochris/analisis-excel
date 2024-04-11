import requests
import pandas as pd

url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    data1 = data['data'][0]
    print(data1)
    print('\n\n')
    
    data = data['data']
    print(data)
    print('\n\n')
    
    df = pd.DataFrame(data)
    print(df)
else:
    print("Failed to retrieve data:", response.status_code)