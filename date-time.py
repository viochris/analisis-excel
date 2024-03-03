from datetime import datetime
import pandas as pd

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime('%H:%M:%S')

df= pd.DataFrame({
    'date-time': [now for i in range(2)],
    'date': [formatted_date for i in range(2)],
    'time': [formatted_time for i in range(2)]
})
df['date-time'] = pd.to_datetime(df['date-time'])

print(df)
df['date2'] = now.strftime("%Y-%m-%d")
df['time2'] = now.strftime('%H:%M:%S')

print(df)
df['date2'] = pd.to_datetime(df['date2'])
df['time2'] = pd.to_datetime(df['time2'])
print(df.dtypes)