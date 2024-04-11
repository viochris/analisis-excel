import pandas as pd
import requests

url = 'https://randomuser.me/api/'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    data1 = data['results'][0]
    print(data1)
    print()
    data = data['results'][0]
    print(data)
    
    df = pd.DataFrame({
    "Gender": [data["gender"]],
    "Title": [data["name"]["title"]],
    "First Name": [data["name"]["first"]],
    "Last Name": [data["name"]["last"]],
    'Full Name': [data['name']['title'] + ' ' + data["name"]["first"] + ' ' + data["name"]["last"]],
    "Street Number": [data["location"]["street"]["number"]],
    "Street Name": [data["location"]["street"]["name"]],
    "City": [data["location"]["city"]],
    "State":[data["location"]["state"]],
    "Country": [data["location"]["country"]],
    })
    print(df)
    
else:
    print("Failed to retrieve data:", response.status_code)