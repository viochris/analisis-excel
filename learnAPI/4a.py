import requests
import pandas as pd

data_kota = pd.DataFrame({
    'Kota' : ['Indonesia', 'Japan', 'China', 'Singapore', 'Malaysia']
})

for negara in data_kota['Kota']:
    url = "http://universities.hipolabs.com/search?country=" + str(negara)
    # url = f"http://universities.hipolabs.com/search?country={negara}"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        df = pd.DataFrame(data)
        df['domains'] = df['domains'].apply(lambda x: ''.join(x))
        df['web_pages'] = df['web_pages'].apply(lambda x: ''.join(x))
        print(df)
        print()