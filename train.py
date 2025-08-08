import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# ====== 1. Load training data ======
df = pd.read_csv(r"C:\Users\hp\Downloads\twilio_biomedical\sepsis_sample_data.csv")

# ====== 2. Separate features and target ======
target_column = "SepsisLabel"
X = df.drop(columns=[target_column])
y = df[target_column]

# ====== 3. Save feature names for use in prediction ======
feature_names = X.columns.tolist()
joblib.dump(feature_names, "feature_names.pkl")

# ====== 4. Fit scaler on training features ======
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ====== 5. Train the Random Forest model ======
model = RandomForestClassifier(random_state=42)
model.fit(X_scaled, y)

# ====== 6. Save model & scaler ======
joblib.dump(model, "sepsis_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ Model, scaler, and feature list saved successfully.")


