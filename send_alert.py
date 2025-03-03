import os
from twilio.rest import Client

# Twilio API credentials (Sample Data - Replace with actual credentials)
TWILIO_ACCOUNT_SID = "AC8faeceda2fe455e679c8069f91093835"
TWILIO_AUTH_TOKEN = "424f10f31f44693fa607f5209de9cef3"
TWILIO_PHONE_NUMBER = "+15155795069"  # Twilio sample number
EMERGENCY_CONTACT = "+918220431677"  # Sample emergency contact number

def send_sms_alert(message):
    """
    Send an SMS alert using Twilio API.
    """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=EMERGENCY_CONTACT
        )
        print(f"✅ SMS Alert Sent! Message SID: {message.sid}")
    except Exception as e:
        print(f"❌ Failed to send SMS: {e}")

def send_whatsapp_alert(message):
    """
    Send a WhatsApp alert using Twilio API.
    """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_="whatsapp:" + TWILIO_PHONE_NUMBER,
            to="whatsapp:" + EMERGENCY_CONTACT
        )
        print(f"✅ WhatsApp Alert Sent! Message SID: {message.sid}")
    except Exception as e:
        print(f"❌ Failed to send WhatsApp alert: {e}")

if __name__ == "__main__":
    alert_message = "Vehicle number:TN 04 Z 3535 ,Location:VIT chennai  ,Alert : met with an accident "
    "emergency"" A vehicle accident has been detected. Immediate help is needed!"
    
    print("📡 Sending emergency alerts...")
    send_sms_alert(alert_message)
    send_whatsapp_alert(alert_message)
