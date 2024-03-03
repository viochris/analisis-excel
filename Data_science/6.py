import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score

# Membuat data buatan
data = {
    'Age': [22, 38, 26, 35, 28, 45, 50, 24, 30, 60],
    'Sex': ['male', 'female', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male'],
    'Fare': [7.25, 71.28, 8.05, 53.10, 8.47, 83.48, 26.55, 12.25, 21.08, 77.32],
    'Survived': [0, 1, 1, 1, 0, 1, 1, 0, 1, 0]
}

# Konversi ke DataFrame
df = pd.DataFrame(data)

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

x = df.drop('Survived', axis=1)
y = df['Survived']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

# inisialisasi model
log_reg = LogisticRegression()
grad_boost = GradientBoostingClassifier()
random_forest = RandomForestClassifier()

log_reg.fit(x_train, y_train)
grad_boost.fit(x_train, y_train)
random_forest.fit(x_train, y_train)

# Evaluate models
log_reg_acc = accuracy_score(y_test, log_reg.predict(x_test))
grad_boost_acc = accuracy_score(y_test, grad_boost.predict(x_test))
random_forest_acc = accuracy_score(y_test, random_forest.predict(x_test))

print("Logistic Regression Accuracy:", log_reg_acc)
print("Gradient Boosting Accuracy:", grad_boost_acc)
print("Random Forest Accuracy:", random_forest_acc)

