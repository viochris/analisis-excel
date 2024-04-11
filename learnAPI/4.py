import requests
import pandas as pd

url = "http://universities.hipolabs.com/search?country=United+States"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    df = pd.DataFrame(data)
    df['domains'] = df['domains'].apply(lambda x: ''.join(x))
    df['web_pages'] = df['web_pages'].apply(lambda x: ''.join(x))
    print(df)
else:
    print("Failed to retrieve data:", response.status_code)