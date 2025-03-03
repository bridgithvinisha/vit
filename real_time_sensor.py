import time
import pandas as pd

# Load dataset (Modify the path as needed)
DATASET_PATH = r"C:\Users\tsvin\Documents\accident_alert_system\data\accident_detection_dataset.csv"

# Read the dataset
df = pd.read_csv(DATASET_PATH)

# Select the first 10 rows
df_sample = df.head(10)

def get_real_time_sensor_data(index):
    """
    Retrieve real sensor data row by row.
    
    Params:
    - index (int): The row index to retrieve from the dataset.
    
    Returns:
    - list: [Accel_X, Accel_Y, Accel_Z, Gyro_X, Gyro_Y, Gyro_Z, Speed]
    """
    row = df_sample.iloc[index]
    return [row["Accel_X"], row["Accel_Y"], row["Accel_Z"], row["Gyro_X"], row["Gyro_Y"], row["Gyro_Z"], row["Speed"]]

if __name__ == "__main__":
    print("📡 Collecting real-time sensor data from the dataset...")

    for i in range(len(df_sample)):  # Loop through first 10 rows
        sensor_data = get_real_time_sensor_data(i)
        print(f"📊 Sensor Data {i+1}: {sensor_data}")

        time.sleep(2)  # Simulate real-time data every 2 seconds
