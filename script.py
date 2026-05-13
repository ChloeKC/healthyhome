
# Author: Chloe Croydon 20119102
# Program Description:
# This program welcomes user and facilitates telemetry data retrieval from Sense
# HAT and returns collected environmental data to MQTT broker via json file.

# Import libraries
from sense_hat import SenseHat
import BlynkLib, os, pathlib
from time import sleep
import json

# Define colours
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

# Initialise Sense HAT
sense = SenseHat()
sense.clear()
deviceID = "rpi-01"

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


# Line 33 Function to retrieve sensor data
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
		state = "OK"

	# Create a dictionary
	data = {
		"deviceID": deviceID,
		"temp": round(temp, 2),
		"humidity": round(humdty, 2),
		"state": state
	}

	return data


# Line 60 Main Loop
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
		"Humy:{:.1f}%".format(humdty),
		text_colour=colour,
		scroll_speed=0.08
	)

	# Delay before next reading
	time.sleep(2)

# Line 101 client.publish(topic, json_data)

