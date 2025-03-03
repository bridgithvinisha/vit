async function predictAccident() {
    try {
        const sensorData = {
            Accel_X: parseFloat(document.getElementById("Accel_X").value),
            Accel_Y: parseFloat(document.getElementById("Accel_Y").value),
            Accel_Z: parseFloat(document.getElementById("Accel_Z").value),
            Gyro_X: parseFloat(document.getElementById("Gyro_X").value),
            Gyro_Y: parseFloat(document.getElementById("Gyro_Y").value),
            Gyro_Z: parseFloat(document.getElementById("Gyro_Z").value),
            Speed: parseFloat(document.getElementById("Speed").value)
        };

        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ sensor_data: Object.values(sensorData) })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        document.getElementById("result").textContent = data.prediction;

    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").textContent = "❌ Error: " + error.message;
    }
}
