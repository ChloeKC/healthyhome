#define BLYNK_TEMPLATE_ID "TMPL4SspJfUmI"
#define BLYNK_TEMPLATE_NAME "SensePi"

import BlynkLib
import os
from time import time, sleep
from sense_hat import SenseHat

#initialise SenseHAT
sense = SenseHat()
sense.clear()

# Blynk authentication token
BLYNK_AUTH = os.getenv("BLYNK_AUTH")

# Initialise Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Time before process shuts down
INACTIVITY_TIMEOUT = 30

# Attach last activity
blynk.last_activity = time()

# Handle virtual pin V1 write events
@blynk.on("V1")
def handle_v1_write(value):

	button_value = value[0]

	# Track activity timestamp
	blynk.last_activity = time()

	print(f'Current button value: {button_value}')
	if button_value=="1":
		sense.clear(255,255,255)
	else:
		sense.clear()

# Main Programme loop
if __name__ == "__main__":

	print("Blynk application started. Listening for events...")

	try:
		while True:

			# Process events
			blynk.run()

			# Send temperature to virtual pin V0
			blynk.virtual_write(0,sense.temperature)

			# Send humidity to virtual pin V2
			blynk.virtual_write(2,sense.humidity)

			now = time()

			# If no activity, break loop
			if now - blynk.last_activity > INACTIVITY_TIMEOUT:
				print(f"No activity for {INACTIVITY_TIMEOUT} seconds. Exiting.")
				break

			sleep(2)  # Avoids high CPU usage

	except KeyboardInterrupt:
		print("Blynk application stopped.")
