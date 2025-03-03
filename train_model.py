import os
import joblib
from sklearn.linear_model import LogisticRegression
from data_preprocessing import load_and_preprocess_data

# Correct file path
filepath = r"C:\Users\tsvin\Documents\accident_alert_system\data\accident_detection_dataset.csv"

# Load and preprocess data
X_train, X_test, y_train, y_test, scaler = load_and_preprocess_data(filepath)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# ✅ Ensure models directory exists
models_dir = os.path.join(os.getcwd(), "models")
os.makedirs(models_dir, exist_ok=True)  # Create if it doesn't exist

# ✅ Save model and scaler
joblib.dump(model, os.path.join(models_dir, "accident_model.pkl"))
joblib.dump(scaler, os.path.join(models_dir, "scaler.pkl"))

print("✅ Model training complete! Model saved in 'models/' directory.")
