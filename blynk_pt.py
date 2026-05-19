import BlynkLib
from time import sleep
from sense_hat import SenseHat
from sense_listen import SensorListen
import json

#initialise SenseHAT
sense = SenseHat()
sense.clear()

# Initialise the Blynk instance
blynk = BlynkLib.Blynk("diqtKzHo0qwNPB7vAvPX1eJwwLgiQe0u")

def sense_telemetry(data):

	try:
		payload = json.loads(data)
	except (TypeError, json.JSONDecodeError) as e:
		print(f"Bad JSON in sense_telemetry: {data}")
		return



	device = payload.get("device")
	value = payload.get("value")
	if device != "pir-01" or value != 1:
		return
	blynk.log_event("temp/humdty_event", "Inhospitable Conditions Detected")

# Main Program loop
if __name__ == "__main__":

	print("Blynk application started. Listening for Events...")

	listener = SensorListen(port=5000)
	listener.callback = sense_telemetry
	listener.start()

	while True:
		blynk.run()
