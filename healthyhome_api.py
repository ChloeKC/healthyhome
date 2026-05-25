# Author: Chloe Croydon 20119102
# Healthy Home Flask App

# Program Description:
# Flask API development, creates access to telemetry data by
# exposing API endpoints using HTTP methods.  /api/telemetry
# http://192.168.178.28:5000
# ------------------------------------------------------------

# Import Libraries
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from sense_hat import SenseHat
import json


# Initialize SenseHAT
sense = SenseHat()
sense.clear()
deviceID="rpi"

# Flask App instance
app = Flask(__name__)

# HTML POST/save Function
@app.route('/api/telemetry', methods=['POST'])
def save_data():

	# Return HTML Request Body
	data = request.json

	# Append "a" readings
	with open("telemetry.json", "a") as dump:

		save = dump.write(json.dumps(data) + "\n")

	return jsonify(save)

# HTTP GET Function
@app.route('/api/telemetry', methods=['GET'])
def get_data():

	# Everything JSON
	with open("telemetry.json", "r") as status:

		msg = status.readlines()

	return jsonify(msg)

# Return Rendered Template(render.html)
@app.route('/')
def index():

	with open("telemetry.json","r") as render:

		reading = render.readlines()

		temperature = "temp"

		humidity = "humidity"

		state = "state"

	return render_template('render.html', temperature=temperature, humidity=humidity,state=state)

# Run/Bind API
app.run(host='0.0.0.0', port=5000, debug=True)
