import random
import time

def get_satellite_location():
    """
    Simulate satellite-based GPS location retrieval.
    """
    try:
        # Simulating latitude and longitude
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)

        # Simulating GPS accuracy
        accuracy = round(random.uniform(3, 20), 2)  # Accuracy in meters

        location_data = {
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        }

        return location_data

    except Exception as e:
        print(f"❌ Error retrieving satellite location: {e}")
        return None

if __name__ == "__main__":
    print("🛰 Fetching location from satellite...")
    time.sleep(2)
    location = get_satellite_location()
    if location:
        print(f"📍 Accident Location: {location}")
    else:
        print("⚠️ Failed to retrieve satellite location.")
