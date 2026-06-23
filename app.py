from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Dummy Sensor Data
sensor_data = {
    "temperature": 25,
    "humidity": 60,
    "pressure": 1013
}

# Dashboard Page
@app.route('/')
def home():
    return render_template('index.html')

# Single API Endpoint
@app.route('/sensor', methods=['GET', 'POST'])
def sensor():

    if request.method == 'POST':
        data = request.get_json()

        if 'temperature' in data:
            sensor_data['temperature'] = data['temperature']

        if 'humidity' in data:
            sensor_data['humidity'] = data['humidity']

        if 'pressure' in data:
            sensor_data['pressure'] = data['pressure']

        return jsonify({
            "message": "Sensor data updated successfully"
        })

    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(debug=True)