import joblib
import numpy as np

# ✅ Load trained model and scaler
model = joblib.load("models/accident_model.pkl")  # Load the trained model
scaler = joblib.load("models/scaler.pkl")  # Load the scaler used during training

def predict_accident(sensor_data):
    """
    Predict accident likelihood from new sensor data.
    
    Parameters:
    sensor_data: List or NumPy array of shape (7,)
                 [Accel_X, Accel_Y, Accel_Z, Gyro_X, Gyro_Y, Gyro_Z, Speed]

    Returns:
    str: "Accident Detected!" or "No Accident."
    """
    sensor_data = np.array(sensor_data).reshape(1, -1)
    
    # ✅ Apply the same scaling used during training
    sensor_data_scaled = scaler.transform(sensor_data)
    
    # Make prediction
    prediction = model.predict(sensor_data_scaled)
    
    return "🚨 Accident Detected!" if prediction[0] == 1 else "✅ No Accident."

# Example test case
if __name__ == "__main__":
    # Simulated real-time sensor data [Accel_X, Accel_Y, Accel_Z, Gyro_X, Gyro_Y, Gyro_Z, Speed]
    test_data = [0.5, -0.2, 0.8, 0.1, -0.5, 0.3, 60]  # Example sensor values
    result = predict_accident(test_data)
    
    print(f"🚗 Prediction Result: {result}")
