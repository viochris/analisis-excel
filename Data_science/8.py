from anchor_tabular_explainer import AnchorTabularExplainer
import pandas as pd
import numpy as np

# Contoh data
data = pd.DataFrame({
    'feature1': np.random.rand(100),
    'feature2': np.random.rand(100),
    'label': np.random.randint(0, 2, 100)
})

# Variabel independen
X = data[['feature1', 'feature2']]

# Variabel dependen
y = data['label']

# Inisialisasi AnchorTabularExplainer
explainer = AnchorTabularExplainer(
    class_names=['0', '1'],
    feature_names=['feature1', 'feature2'],
    train_data=X,
    categorical_names={}
)
