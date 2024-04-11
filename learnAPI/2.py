import requests
import pandas as pd

url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    df = pd.DataFrame(data['data'])
    print(df)
else:
    print("Failed to retrieve data:", response.status_code)