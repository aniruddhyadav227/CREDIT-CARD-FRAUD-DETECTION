# 1. Zaroori libraries import karein
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# 2. Dummy Data Create Karna 
# (Kyunki asli Kaggle dataset 150MB+ ka hota hai, testing ke liye hum dummy data bana rahe hain)
np.random.seed(42)
n_samples = 1000

data = {
    'time': np.random.uniform(0, 100000, n_samples),
    'v1': np.random.normal(0, 1, n_samples),
    'v2': np.random.normal(0, 1, n_samples),
    'amount': np.random.uniform(1, 1000, n_samples),
    'is_fraud': np.random.choice([0, 1], n_samples, p=[0.90, 0.10]) # 10% fraud data
}

df = pd.DataFrame(data)

# 3. Data ko Features (X) aur Target (y) me split karna
X = df[['time', 'v1', 'v2', 'amount']]
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Machine Learning Model Train karna
print("Model train ho raha hai...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model training complete!")

# 5. Model ko .pkl file me save karna
# Ye check karega ki models folder hai ya nahi, aur wahan file save karega
os.makedirs('../models', exist_ok=True)
joblib.dump(model, '../models/fraud_model.pkl')

print("✅ Model successfully 'models/fraud_model.pkl' ke naam se save ho gaya hai!")