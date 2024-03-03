import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

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
print("Classification Report:\n", classification_report(y_test, prediction))
print("Confusion Matrix:\n", confusion_matrix(y_test, prediction))

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15]
}
# merupakan pilihan

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3)
# tahap pencarian
grid_search.fit(x_train, y_train)
# tahap pencarian dilakukan dan dilakukan pelatihan dan penerepan

best_model = grid_search.best_estimator_
# hasil grid_search.fit(x_train, y_train) terbaik diambil lalu digunakan di bawah ini
best_prediction = best_model.predict(x_test)

# Evaluate the Best Model
print("\nBest Model:", best_model)
print("Accuracy: ", accuracy_score(y_test, best_prediction))
print("Classification Report:\n", classification_report(y_test, best_prediction))
print("Confusion Matrix:\n", confusion_matrix(y_test, best_prediction))

# Feature Importance
feature_importances = pd.DataFrame({'Feature': x.columns, 'Importance': model.feature_importances_})
print("\nFeature Importance:\n", feature_importances)