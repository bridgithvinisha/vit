Overview

This project is an Accident Detection System for Electric Vehicles, which uses real-time sensor data, AI-based accident detection, cloud storage, and automated emergency alerts. The system includes:

AI-based accident prediction using sensor data

Firebase integration for cloud storage

Twilio API for emergency SMS alerts

Flask backend for processing and serving predictions

React frontend for user interaction

(Future) Satellite communication for remote areas

📂 Project Structure

accident_alert_system/
│-- models/                 # Trained ML model and scaler
│   ├── accident_model.pkl   # Trained accident detection model
│   ├── scaler.pkl           # Scaler for preprocessing sensor data
│
│-- src/                    # Source code
│   ├── backend.py           # Flask backend for prediction
│   ├── firebase_integration.py  # Firebase storage handler
│   ├── send_alert.py        # Twilio-based SMS alerts
│   ├── satellite_communication.py  # Placeholder for satellite API
│
│-- frontend/                # Frontend UI (React/HTML/CSS)
│   ├── index.html           # Main UI page
│   ├── script.js            # JavaScript logic for fetching predictions
│   ├── styles.css           # CSS styles for UI
│
│-- firebase_config.json     # Firebase credentials (Add manually)
│-- README.md                # Project documentation



Installation

1️⃣ Clone the Repository
git clone https://github.com/your-repo/accident_alert_system.git
cd accident_alert_system

2️⃣ Set Up Python Virtual Environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run the Backend
python src/backend.py

6️⃣ Start the Frontend
cd frontend
npm install
npm start

For HTML/JS: Simply open frontend/index.html in a browser.

How It Works
1.Real-time sensor data is collected (e.g., acceleration, gyroscope, speed)
2.AI model predicts accident likelihood
3.Twilio sends an SMS alert to emergency contacts
(Future) Satellite API sends data to remote responders


 Future Enhancements
1.GPS tracking for real-time accident location
2.Mobile app integration
3.Machine learning model improvement with more training data



