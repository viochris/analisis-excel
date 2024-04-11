import pandas as pd
import requests

url = 'https://randomuser.me/api/'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    results = data['results']
    
    df_list = []
    
    for entry in results:
        df_entry = {
            "Gender": entry["gender"],
            "Title": entry["name"]["title"] + '.',
            "First Name": entry["name"]["first"],
            "Last Name": entry["name"]["last"],
            'Full Name': entry['name']['title'] + '.' + ' ' + entry["name"]["first"] + ' ' + entry["name"]["last"],
            # "Street Number": entry["location"]["street"]["number"],
            # "Street Name": entry["location"]["street"]["name"],
            "City": entry["location"]["city"],
            "State": entry["location"]["state"],
            "Country":entry["location"]["country"],
        }
        df_list.append(df_entry)
    
    df = pd.DataFrame(df_list)
    print(df)
else:
    print("Failed to retrieve data:", response.status_code)