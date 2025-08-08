import pandas as pd
import joblib
from twilio.rest import Client

# Load saved model, scaler & feature list
model = joblib.load("sepsis_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

# Load test data
test_df = pd.read_csv(r"C:\Users\hp\Downloads\twilio_biomedical\test_data.csv")

# Remove label if present
target_column = "SepsisLabel"
if target_column in test_df.columns:
    X_test = test_df.drop(columns=[target_column])
else:
    X_test = test_df.copy()

# Match feature order
missing_features = set(feature_names) - set(X_test.columns)
if missing_features:
    raise ValueError(f"Missing features in test data: {missing_features}")
X_test = X_test[feature_names]

# Scale features
X_test_scaled = scaler.transform(X_test)

# Predictions
predictions = model.predict(X_test_scaled)

# Debug print
print("\n=== Prediction Results ===")
for i, pred in enumerate(predictions):
    print(f"Patient {i+1}: Prediction={pred}, Vitals={X_test.iloc[i].to_dict()}")

# Twilio setup
account_sid = "ACd4052c916008626174e5017a3570fd5b"
auth_token = "fd05eb12160ffacaa68278831b440c67"
twilio_number = "+18155154790"
receiver_number = "+917876568316"

client = Client(account_sid, auth_token)

# Send alerts
alerts_sent = 0
for i, pred in enumerate(predictions):
    if pred == 1:
        patient_info = X_test.iloc[i].to_dict()
        message_text = (
            f"🚨 Sepsis Risk Alert 🚨\n"
            f"Patient #{i+1} may be at risk.\n"
            f"Vitals: HR={patient_info.get('HR', 'N/A')}, "
            f"Temp={patient_info.get('Temp', 'N/A')}, "
            f"WBC={patient_info.get('WBC', 'N/A')}, "
            f"RR={patient_info.get('RR', 'N/A')}, "
            f"Age={patient_info.get('Age', 'N/A')}"
        )

        message = client.messages.create(
            body=message_text,
            from_=twilio_number,
            to=receiver_number
        )
        alerts_sent += 1
        print(f"📩 SMS sent for Patient {i+1}. SID: {message.sid}")

if alerts_sent == 0:
    print("✅ No patients at risk. No alerts sent.")
else:
    print(f"✅ Alert process completed. {alerts_sent} SMS sent.")
