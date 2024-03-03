import unittest
import numpy as np
from sklearn.linear_model import LinearRegression


        # Persiapan data
X_train = np.array([[1], [2], [3], [4], [5], [6], [7]])
y_train = np.array([1, 4, 9, 16, 25, 36, 49])
        
        # Membuat model
model = LinearRegression()
model.fit(X_train, y_train)
        
        # Melakukan prediksi
X_test = np.array([[10]])
y_pred = model.predict(X_test)
print(y_pred)
        

