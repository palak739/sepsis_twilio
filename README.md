🚨 Early Sepsis Detection System with Twilio SMS Alerts
This project is a machine learning-based early warning system for detecting potential sepsis cases in patients based on vital signs and lab results.
If a patient is predicted to be at risk, the system automatically sends a real-time SMS alert using Twilio.

📌 Features
Machine Learning Model: Trained using a Random Forest Classifier.

Automatic Scaling: Uses StandardScaler to normalize input features.

Twilio SMS Alerts: Sends alerts instantly to a configured phone number.

Customizable Thresholds: Modify logic to tune sensitivity.

Batch Processing: Can handle multiple patient records at once.

📂 Project Structure
📁 sepsis_detection
 ├── train_model.py          # Trains and saves ML model + scaler
 ├── predict_and_alert.py    # Loads model, predicts, sends SMS
 ├── sepsis_sample_data.csv  # Training dataset
 ├── test_data.csv           # Test dataset for predictions
 ├── sepsis_model.pkl        # Saved ML model
 ├── scaler.pkl              # Saved feature scaler
 ├── README.md               # Project documentation

⚙️ Requirements
Install dependencies with:
pip install pandas scikit-learn twilio joblib
