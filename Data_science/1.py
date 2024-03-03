import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


data = {
    'feature_1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'feature_2': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'target_column': ['No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)

x = df[['feature_1', 'feature_2']]
y = df['target_column']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, max_depth=10,random_state=42)
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print(prediction)
print("Accuracy: ",accuracy_score(y_test, prediction))

prediction = model.predict([[1, 1]])
print(prediction)

new_data = pd.DataFrame({
    'feature_1': [input('Masukkan nomor disini: ')],
    'feature_2': [input('Disini Juga: ')]
})
prediction = model.predict(new_data)
print(prediction)



jumlah = int(input('Ingin mencoba berapa kali? '))
new_data = {
    'feature_1': [],
    'feature_2': []
}
for i in range(jumlah):
    input_1 = input('Masukkan data 1: ')
    input_2 = input('Masukkan data 2: ')
    
    new_data['feature_1'].append(input_1)
    new_data['feature_2'].append(input_2)
df = pd.DataFrame(new_data)
prediction = model.predict(df)
print(prediction)