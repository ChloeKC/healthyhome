
# Author: Chloe Croydon 20119102
# Program Description:
# This program welcomes user and facilitates data retrieval from Sense 
# HAT and returns collected environmental data to 

# Import libraries
from sense_hat import SenseHat
import time

# Define colours
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

# Initialise Sense HAT
sense = SenseHat()
sense.clear()

# User greeting
sense.show_message("Hello!", scroll_speed=0.05, text_colour=[255, 0, 0])

# Create function that returns data variables
def get_env_data():

	# Read sensor data and retrieve current temperature and humidity
	temp = sense.get_temperature()
	humdty = sense.get_humidity()

	# Return values
	return temp, humdty

	# Create a dictionary
#	data = {
#		"deviceID": deviceID,
#		"temp": round(temp, 2),
#		"humidity": round(humdty, 2)
#		}
#
#	return data

while True:

	# Get readings
	temp, humdty = get_env_data()

	# Print to command line
	print("Temperature: {:.1f} C Humidity: {:.1f} %"
	.format(temp, humdty))

	# Display on LED matrix
	sense.show_message("T:{:.1f}C".format(temp), text_colour=RED)
	sense.show_message("H:{:.1f}%".format(humdty), text_colour=BLUE)

	# 2 second delay before next reading
	time.sleep(2)

# Allow standalone testing
#if __name__ == "__main__":

	# Example device ID and usage
#	deviceID = "myDevice1"
#	env_data = get_environmental_data(deviceID)

	# Print the data in JSON format for testing
#	print(env_data)
