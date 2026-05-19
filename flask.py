from flask import Flask, request
import requests
import json
from flask_cors import CORS
from sense_hat import SenseHat

# Create Flask app instance
app = Flask(__name__)

# Define SAVE data function
@app.route('/api/telemetry', methods=['POST'])

def save_data():

	data = request.json

	with open("telemetry.json", "a") as f:
        f.write(json.dumps(data) + "\n")

    return {"status": "saved"}

# Define GET data function
@app.route('/api/telemetry', methods=['GET'])

def get_data():

    with open("telemetry.json", "r") as f:
        lines = f.readlines()

    return lines

# Run API on port 5000
app.run(host='0.0.0.0', port=5000, debug=True)
