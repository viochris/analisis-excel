import pandas as pd
import requests

url = 'https://api.zippopotam.us/us/33162'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    results = data['places']
    
    df_list = []
    
    for entry in results:
        df_entry = pd.DataFrame({
            'post_code' : [data['post code']],
            'country' : [data['country']],
            'country_abbreviation' : [data['country abbreviation']],
            'place' : entry['place name'],
            'state' : entry['state'],
            'state_abbreviation' : entry['state abbreviation'],
            'longitude' : entry['longitude'],
            'latitude' : entry['latitude']
        })
        df_list.append(df_entry)
    
    df = pd.concat(df_list, ignore_index=True)
    print(df)
else:
    print("Failed to retrieve data:", response.status_code)