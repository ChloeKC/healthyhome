# Author: Chloe Croydon 20119102
# Blynk Program Description:
# Blynk, Packet Tracer & IoT application for monitoring simulated
# environmental conditions using Raspberry Pi and Sense HAT.

import BlynkLib
from time import sleep
from sense_hat import SenseHat
from sense_listen import SensorListen
import json

# Initialise SenseHAT
sense = SenseHat()
sense.clear()

# Initialise the Blynk instance
blynk = BlynkLib.Blynk("diqtKzHo0qwNPB7vAvPX1eJwwLgiQe0u")

# Handle telemetry callback
def sense_telemetry(payload):

	try:
		print(payload)

		device = payload.get("device")
		state = payload.get("state")

	except (TypeError, json.JSONDecodeError) as e:
		print(f"Bad JSON in sense_telemetry: {payload}")
		return

	device = payload.get("device")
	state = payload.get("state")

	# Trigger alert

	if device != "rpi-01" or value != 1:
		return

	blynk.log_event("event_alert", "Inhospitable Conditions Detected")

# Main Program loop
if __name__ == "__main__":

	print("Blynk application started. Listening for Events...")

	listener = SensorListen(port=5005)
	listener.callback = sense_telemetry
	listener.start()

	while True:
		blynk.run()
		sleep(0.1)
