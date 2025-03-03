import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Use raw string or double backslashes to avoid Unicode errors
filepath = r"C:\Users\tsvin\Documents\accident_alert_system\data\accident_detection_dataset.csv"

def load_and_preprocess_data(filepath):
    # Load dataset
    df = pd.read_csv(filepath)

    # Features & labels
    X = df[["Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Speed"]]
    y = df["Crash_Label"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalize using StandardScaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

# Test function
if __name__ == "__main__":
    X_train, X_test, y_train, y_test, scaler = load_and_preprocess_data(filepath)
    print("✅ Data Preprocessing Successful!")
