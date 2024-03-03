import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = {
    'feature_1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15],
    'feature_2': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1,1,1,1,0,0],
    'target_column': ['No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No']
}
df = pd.DataFrame(data)

x = df[['feature_1', 'feature_2']]
y = df['target_column']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, max_depth=50,random_state=42)
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print(prediction)
print("Accuracy: ",accuracy_score(y_test, prediction))

new_data = pd.DataFrame({
    'feature_1': [10,9,1,12,3],
    'feature_2': [0,1,1,0,1]
})
prediction = model.predict(new_data)
print(prediction)
print("Accuracy: ",accuracy_score(y_test, prediction))

new_data = pd.DataFrame({
    'feature_1': [1,9,10,11,12],
    'feature_2': [1,1,1,0,1]
})
prediction = model.predict(new_data)
print(prediction)
print("Accuracy: ",accuracy_score(y_test, prediction))

print("Classification Report:\n", classification_report(y_test, prediction))
print("Confusion Matrix:\n", confusion_matrix(y_test, prediction))