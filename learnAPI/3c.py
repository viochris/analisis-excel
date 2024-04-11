import pandas as pd
import requests

url = 'https://randomuser.me/api/'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    results = data['results']
    print(results)
    
    df_list = []
    
    for entry in results:
        Gender= entry["gender"]
        Title= entry["name"]["title"] + '.'
        First_Name= entry["name"]["first"]
        Last_Name= entry["name"]["last"]
        Full_Name= entry['name']['title']+ '.' + ' ' + entry["name"]["first"] + ' ' + entry["name"]["last"]
        # Street_Number= entry["location"]["street"]["number"]
        # Street_Name= entry["location"]["street"]["name"]
        City= entry["location"]["city"]
        State= entry["location"]["state"]
        Country=entry["location"]["country"]
        data = [Gender, Title, First_Name, Last_Name, Full_Name, City, State, Country]
        df_list.append(data)

    labels = ['Gender', 'Title', 'First_Name', 'Last_Name', 'Full_Name', 'City', 'State', 'Country']
    df = pd.DataFrame(df_list, columns = labels)
    print(df)
else:
    print("Failed to retrieve data:", response.status_code)