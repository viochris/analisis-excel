import requests
import pandas as pd

url = "https://api.zippopotam.us/us/33162"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data['places'])
    print(df)
    
    penyimpanan = []
    

    post_code = data['post code']
    country = data['country']
    country_abbreviation = data['country abbreviation']
    for entry in data['places']:
        place = entry['place name']
        state = entry['state']
        state_abbreviation = entry['state abbreviation']
        longitude = entry['longitude']
        latitude = entry['latitude']
        masuk = [post_code, country, country_abbreviation, place, state, state_abbreviation, longitude, latitude]
        penyimpanan.append(masuk)
    
    labels = ['post code', 'country', 'country abbreviation', 'place name', 'state', 'state abbreviation', 'longitude', 'latitude']
    df = pd.DataFrame(penyimpanan, columns = labels)
    print(df)
        
else:
    print("Failed to retrieve data:", response.status_code)
