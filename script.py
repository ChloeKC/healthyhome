# Author: Chloe Croydon 20119102
# Healthy Home Sense Script

# Program Description:
# RPi & Python program facilitates telemetry data retrieval from SenseHAT
# and forwards collected environmental data to Flask/Blynk via json file.
# ------------------------------------------------------------------------

# Import Libraries
from sense_hat import SenseHat
import os
import json
import time
from time import sleep
import requests

# Initialise Sense HAT
sense = SenseHat()
sense.clear()
deviceID = "rpi"

# Define Colours
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255, 255, 255)

# Greeting
sense.show_message(
	"Hi Healthy Home Hacker",
	scroll_speed=0.05,
	text_colour=GREEN
)

# Environmental Telemetry Function:
# --------------------------------
# Note: Temperature and Humidity readings can be influenced
#       by heat from RPi's CPU. The humidity sensor on the SenseHAT
#	generally reads too low because it is affected by heat.
#	Raw data is calibrated to for accuracy.

def get_env_data():

	# Read/calibrate
	temp = round(sense.get_temperature() - 7, 2)
	humdty = round(sense.get_humidity() - 10, 2)

	# Determine state
	if temp > 25 or humdty > 70:
		state = "HIGH"

	elif temp < 18 or humdty < 35:
		state = "LOW"

	else:
		state = "SAUL GOOD"

	# Dictionary
	data = {
		"deviceID": deviceID,
		"temperature": temp,
		"humidity": humdty,
		"state": state
	}

	return data


# Main Loop:
# ----------

while True:

	# Get readings
	data = get_env_data()

	deviceID = data["deviceID"]
	temp = data["temperature"]
	humdty = data["humidity"]
	state = data["state"]

	# Print to CLI
	print(
		"Temperature: {:.1f} C Humidity: {:.1f} % | State: {}"
		.format(temp, humdty, state)
	)

	# Print to JSON
	print(json.dumps(data, indent=4))

	# Send to Flask
	requests.post(
		"http://localhost:5000/api/telemetry",json=data
	)

	# LED Logic
	if state == "HIGH":
    		colour = RED

	elif state == "LOW":
    		colour = BLUE

	else:
    		colour = GREEN


	# Display Temperature:
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
