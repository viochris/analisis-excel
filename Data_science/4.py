import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

np.random.seed(42)
data = {
    'feature_1': np.random.rand(100),
    'feature_2': np.random.randint(0,2,100),
    'target': np.random.choice(['No', 'Yes'], 100)
}

df = pd.DataFrame(data)

# Data Exploration
print("Data Overview:")
print(df.head())
print(df.info())

# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='feature_1', y='feature_2', hue='target', data=df)
# plt.title('Scatter Plot')
# plt.show()

x = df[['feature_1', 'feature_2']]
y = df['target']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, max_depth=10,random_state=42)
model.fit(x_train, y_train)

prediction = model.predict(x_test)
print(x_test)
print(prediction)
print("Accuracy: ",accuracy_score(y_test, prediction))
print("Classification Report:")
print(classification_report(y_test, prediction))
conf_matrix = confusion_matrix(y_test, prediction)
print(conf_matrix)


sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=True)
plt.title('Confusion Matrix')
plt.show()


