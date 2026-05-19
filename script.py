# Author: Chloe Croydon 20119102
# sense_script Program Description:
# RPi & Python program facilitates telemetry data retrieval from Sense
# HAT and forwards collected environmental data to Blynk via json file.

# Import libraries
from sense_hat import SenseHat
import BlynkLib, os, pathlib
import os, json, datetime, time
from time import sleep
from flask import Flask, requests
from flask_cors import CORS

# Initialise Sense HAT
sense = SenseHat()
sense.clear()
deviceID = "rpi-01"

# Define colours
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255, 255, 255)

# Greeting
sense.show_message(
	"Hello Healthy Home Hacker",
	scroll_speed=0.05,
	text_colour=GREEN
)

# Note: Temperature and Humidity readings can be influenced
#       by heat from RPi's CPU. The humidity sensor on the SenseHAT
#	generally reads too low because it is affected by heat.
#	Raw data is calibrated to for accuracy.

# Create Flask app instance
app = Flask(__name__)
CORS(app)

# Function to retrieve calibrated sensor data
def get_env_data():

	# Read sensor data
	temp = round(sense.get_temperature() - 7, 2)
	humdty = round(sense.get_humidity() - 10, 2)

	# Determine state
	if temp > 25 or humdty > 70:
		state = "WARNING"

	elif temp < 18 or humdty < 35:
		state = "LOW"

	else:
		state = "GOOD"

	# Create dictionary
	data = {
		"deviceID": deviceID,
		"temp": round(temp, 2),
		"humidity": round(humdty, 2),
		"state": state
	}

	return data


# Main Loop
while True:

	# Get readings
	data = get_env_data()

	deviceID = data["deviceID"]
	temp = data["temp"]
	humdty = data["humidity"]
	state = data["state"]

	# Print to command line
	print(
		"Temperature: {:.1f} C Humidity: {:.1f} % | State: {}"
		.format(temp, humdty, state)
	)

	# Print telemetry
	print(json.dumps(data, indent=4))

	# Send data to Flask
	requests.post(
		"http://localhost:5000/api/telemetry",json=data
	)

	# LED colour logic
	if state == "WARNING":
    		colour = RED

	elif state == "LOW":
    		colour = BLUE

	else:
    		colour = GREEN


	# Display temperature:
	sense.show_message(
		"Temp:{:.1f}C".format(temp),
		text_colour=colour,
		scroll_speed=0.05
	)

	# Display Humidity:
	sense.show_message(
		"Humdty:{:.1f}%".format(humdty),
		text_colour=colour,
		scroll_speed=0.05
	)

	# Delay before next reading
	time.sleep(5)
