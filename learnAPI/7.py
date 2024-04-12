import requests
import json
import pandas as pd

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    # data = response.json()

    
    df = pd.DataFrame({
        'Joke': data
        })
    print(df)
    
    df = pd.DataFrame({
        1: data
        })
    print(df)
    
    df = pd.DataFrame({
        1: data
        }).T
    print(df)
else:
    print("Failed to retrieve data:", response.status_code)