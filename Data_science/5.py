# import lime 
# import eli5
# import xgboost
# import anchor
# import jax as jx
# import jaxlib as jxl
# import mxnet as mx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score
import shap
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Data Generation
np.random.seed(42)
data = {
    'feature_1': np.random.rand(100),
    'feature_2': np.random.randint(0, 2, 100),
    'target': np.random.choice(['No', 'Yes'], 100)
}
df = pd.DataFrame(data)

label_encoder = LabelEncoder()
df['target'] = label_encoder.fit_transform(df['target'])

# Data Exploration
print("Data Overview:")
print(df.head())
print(df.info())

x = df[['feature_1', 'feature_2']]
y = df['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print(prediction)

print("Accuracy: ", accuracy_score(y_test, prediction))
print("Classification Report:")
print(classification_report(y_test, prediction))
conf_matrix = confusion_matrix(y_test, prediction)
print(conf_matrix)

scores = cross_val_score(model, x,y,cv=5)
print(scores)
print("Cross-validated accuracy:", np.mean(scores))

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15]
}
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3)
grid_search.fit(x_train, y_train)
best_model = grid_search.best_estimator_
print('Best Model: ', best_model)
print('Best Model Params: ', grid_search.best_params_)
best_prediction = best_model.predict(x_test)
print(best_prediction)

print("Accuracy: ", accuracy_score(y_test, best_prediction))
print("Classification Report:")
print(classification_report(y_test, best_prediction))
conf_matrix = confusion_matrix(y_test, best_prediction)
print(conf_matrix)

df['feature_3'] = df['feature_1'] * df['feature_2']


gb_model = GradientBoostingClassifier(n_estimators=100, max_depth=3, random_state=42)
gb_model.fit(x_train, y_train)  # Melatih model menggunakan data latih
predictions = gb_model.predict(x_test)  # Melakukan prediksi pada data uji
print(predictions)
accuracy = accuracy_score(y_test, predictions)  # Mengukur akurasi model
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, predictions))
conf_matrix = confusion_matrix(y_test, predictions)
print(conf_matrix)
scores = cross_val_score(gb_model, x,y,cv=5)
print(scores)
print("Cross-validated accuracy:", np.mean(scores))

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(x_test)
# shap.summary_plot(shap_values, x_test, plot_type="bar")

tf.compat.v1.disable_eager_execution()
model_dl = Sequential([
    Dense(64, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])
model_dl.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_dl.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))