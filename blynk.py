# Author: Chloe Croydon 20119102
# Blynk Program Description:
# Blynk & IoT application for monitoring and controlling
# environmental conditions using Raspberry Pi and Sense HAT.

# define BLYNK_TEMPLATE_ID
BLYNK_TEMPLATE_ID="TMPL4SspJfUmI"
# define BLYNK_TEMPLATE_NAME
BLYNK_TEMPLATE_NAME="SensePi"

# Import libraries
import BlynkLib
import os
from time import time, sleep
from sense_hat import SenseHat

# Initialise Sense HAT
sense = SenseHat()
sense.clear()
deviceID = "rpi"

# Define colours
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255, 255, 255)

# Blynk authentication token
BLYNK_AUTH = os.getenv("BLYNK_AUTH")

# Initialise Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Time before process shuts down
INACTIVITY_TIMEOUT = 130

# Attach last activity
blynk.last_activity = time()

# Function to retrieve calibrated values
def get_env_data():

	temp = sense.get_temperature() - 7
	humdty = sense.get_humidity() - 10

	if temp > 25 or humdty > 70:
		state = "WARNING"

	elif temp < 18 or humdty < 35:
		state = "LOW"

	else:
		state = "GOOD"

	return temp, humdty, state

# Handle virtual pin V1 write events
@blynk.on("V1")
def handle_v1_write(value):

	button_value = value[0]

	# Update activity timestamp
	blynk.last_activity = time()

	print(f'Button value: {button_value}')

	if button_value=="1":
		sense.clear(255,255,255)
	else:
		sense.clear()

# Main Programme loop
if __name__ == "__main__":

	print("Blynk application started. Listening for events...")

	try:
		while True:

			# Process Blynk events
			blynk.run()

			# Get telemetry
			temp, humdty, state = get_env_data()

			# Print readings
			print("Temperature: {:.1f} C | Humidity: {:.1f}% | State: {}".format(temp, humdty, state))

			# Send telemetry to dashboard
			blynk.virtual_write(0, temp)
			blynk.virtual_write(2, humdty)
			blynk.virtual_write(3, state)

			now = time()

			# If no activity, break loop
			if now - blynk.last_activity > INACTIVITY_TIMEOUT:

				print(f"No activity for {INACTIVITY_TIMEOUT} seconds. Exiting.")
				break

			sleep(2)  # Avoids high CPU usage

	except KeyboardInterrupt:
		print("Blynk application stopped.")
