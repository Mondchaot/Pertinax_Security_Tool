from sklearn.ensemble import IsolationForest
import numpy as np

class AIAnalyzer:
    def __init__(self):
        self.model = IsolationForest(n_estimators=100)
        self.is_trained = False

    def train(self, dataset):
        X = np.array(dataset).reshape(-1, 1)
        self.model.fit(X)
        self.is_trained = True

    def predict(self, value):
        if not self.is_trained:
            raise ValueError("Model not trained.")
        return self.model.predict([[value]])[0]  # 1 = normal, -1 = anomaly