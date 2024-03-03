from datetime import datetime, timedelta
import pandas as pd

now = datetime.now().date()
two_weeks_ago1 = now - timedelta(weeks=2)
two_weeks_ago2 = now - timedelta(days = 14)
print(two_weeks_ago1)
print(two_weeks_ago2)

two_weeks_ago = datetime.now() - timedelta(weeks=2)


df = pd.DataFrame({
    'Date': ['2024-02-25', '2024-03-16', '2024-02-01', '2024-05-10', '2024-04-01'],
    'Terjual': ['Sapu', 'Sapi', 'Engkrak', 'Nasgor', 'sushi']
})
df['Date'] = pd.to_datetime(df['Date'])
print(df)
df = df[df['Date'] >= two_weeks_ago]
print(df)