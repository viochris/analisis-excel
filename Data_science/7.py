import numpy as np
from anchor import anchor_tabular

# Contoh data
X = np.random.rand(100, 5)
y = np.random.randint(2, size=100)

# Inisialisasi model
class Model:
    def predict(self, X):
        return np.random.randint(2, size=len(X))

# Membuat anchor
explainer = anchor_tabular.AnchorTabularExplainer(class_names=['0', '1'], feature_names=['feature1', 'feature2', 'feature3', 'feature4', 'feature5'], train_data=X)

# Memperoleh anchor untuk sampel pertama
idx = 0
anchor = explainer.explain_instance(X[idx], Model().predict, threshold=0.95)
print('Anchor: %s' % (' AND '.join(anchor.names())))

