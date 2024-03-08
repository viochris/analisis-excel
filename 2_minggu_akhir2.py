from datetime import date, timedelta
import pandas as pd

now = date.today()
two_weeks_ago1 = now - timedelta(weeks=2)
two_weeks_ago2 = now - timedelta(days = 14)
two_weeks_ago3 = now - timedelta(weeks = 4)
two_weeks_ago4 = now - timedelta(days = 30)
print(two_weeks_ago1)
print(two_weeks_ago2)
print(two_weeks_ago3)
print(two_weeks_ago4)


two_weeks_ago = pd.to_datetime(date.today() - timedelta(weeks=2))


df = pd.DataFrame({
    'Date': ['2024-02-25', '2024-03-16', '2024-02-01', '2024-05-10', '2024-04-01'],
    'Terjual': ['Sapu', 'Sapi', 'Engkrak', 'Nasgor', 'sushi']
})
df['Date'] = pd.to_datetime(df['Date'])
df['Date-bulan'] = pd.to_datetime(df['Date'].dt.strftime("%m-%d"), format='%m-%d')
df['Date-tahun'] = pd.to_datetime(df['Date'].dt.strftime("%Y-%m"), format='%Y-%m')
df['Date-bln'] = df['Date'].dt.strftime("%b-%Y")
df['Date-bln'] = pd.to_datetime(df['Date-bln'])
print(df)
df = df[df['Date'] >= two_weeks_ago]
print(df)
print(df.dtypes)