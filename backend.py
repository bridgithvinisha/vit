from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS  # Enable frontend-backend communication

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# Load trained model and scaler
model = joblib.load("models/accident_model.pkl")  # Ensure path is correct
scaler = joblib.load("models/scaler.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        sensor_data = np.array(data["sensor_data"]).reshape(1, -1)
        
        # Scale data
        sensor_data_scaled = scaler.transform(sensor_data)
        
        # Make prediction
        prediction = model.predict(sensor_data_scaled)
        
        result = "🚨 Accident Detected!" if prediction[0] == 1 else "✅ No Accident."
        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
