Creating an IoT-based platform to monitor real-time environmental conditions is an exciting project. Below, I'll provide a Python program that simulates the core functionality of an environment sensor dashboard. This mock-up will include data simulation for various sensors, a simple HTTP server to display the data, and basic error handling. This example will be limited in scope without actual IoT hardware or network communication, but it will give you a foundation to build upon.

```python
import random
import json
from flask import Flask, jsonify, render_template

# Flask app initialization
app = Flask(__name__)

def simulate_environment_data():
    """
    Simulate environmental data from various sensors.
    For demonstration purposes, will generate random data.
    """
    try:
        data = {
            "temperature": round(random.uniform(15.0, 30.0), 2),  # Celsius
            "humidity": round(random.uniform(30.0, 70.0), 2),     # Percentage
            "air_quality": round(random.uniform(10.0, 100.0), 2), # Air quality index
            "light_level": round(random.uniform(100.0, 1000.0), 2) # Lux
        }
        return data
    except Exception as e:
        print(f"Error while simulating environmental data: {e}")
        return None

@app.route('/api/data')
def get_data():
    """
    Endpoint to get the simulated environmental data.
    """
    try:
        data = simulate_environment_data()
        if data:
            return jsonify(data)
        else:
            return jsonify({"error": "Failed to generate data"}), 500
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {e}"}), 500

@app.route('/')
def index():
    """
    Serve the dashboard.
    """
    try:
        return render_template('dashboard.html')
    except Exception as e:
        return f"Error loading dashboard: {e}", 500

# HTML template for dashboard
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Environment Sensor Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        #data-container { padding: 20px; }
        .sensor { padding: 10px; }
    </style>
    <script>
        function fetchSensorData() {
            fetch('/api/data')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('temperature').innerText = 'Temperature: ' + data.temperature + ' °C';
                    document.getElementById('humidity').innerText = 'Humidity: ' + data.humidity + ' %';
                    document.getElementById('air_quality').innerText = 'Air Quality: ' + data.air_quality;
                    document.getElementById('light_level').innerText = 'Light Level: ' + data.light_level + ' Lux';
                })
                .catch(error => console.error('Error fetching data:', error));
        }

        setInterval(fetchSensorData, 5000); // Fetch data every 5 seconds
        window.onload = fetchSensorData;
    </script>
</head>
<body>
    <div id="data-container">
        <h1>Real-Time Environment Sensor Dashboard</h1>
        <div class="sensor" id="temperature">Temperature: -- °C</div>
        <div class="sensor" id="humidity">Humidity: -- %</div>
        <div class="sensor" id="air_quality">Air Quality: --</div>
        <div class="sensor" id="light_level">Light Level: -- Lux</div>
    </div>
</body>
</html>
"""

@app.route('/dashboard.html')
def dashboard():
    """
    Serve the HTML template.
    """
    return HTML_TEMPLATE

if __name__ == '__main__':
    # Run the Flask app with error handling
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting Flask server: {e}")
```

### Key Components:
- **Flask App**: Provides a basic web server to host a dashboard.
- **Simulated Sensor Data**: Utilizes Python's `random` library to generate pseudo-realistic environmental data.
- **Endpoints**: 
  - `/api/data` returns simulated sensor data in JSON format.
  - `/` serves the main dashboard page using an HTML template.
- **Dashboard UI**: A basic web page using HTML and JavaScript to periodically fetch and display the sensor data.

This is a basic simulation and you would typically replace the data simulation part with actual sensor data collection from IoT devices. Further improvements could include adding authentication, data storage, and more advanced error handling mechanisms.