import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

print("⏳ Machine Learning Model train ho raha hai, thoda wait karein...")

# Models folder automatically banayega
os.makedirs('models', exist_ok=True)

# Dummy dataset generate karna (Kyunki real dataset bahut bada hota hai)
np.random.seed(42)
n_samples = 1000
X = np.random.uniform(0, 1000, (n_samples, 4)) # Time, V1, V2, Amount
y = np.random.choice([0, 1], n_samples, p=[0.90, 0.10]) # 10% fraud cases

# Model Train karna
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

# Model ko save karna
joblib.dump(model, 'models/fraud_model.pkl')
print("✅ Model successfully 'models/fraud_model.pkl' me save ho gaya!")