import socket
import threading
import json
import requests
from time import sleep

# Encapsulation
class SensorListen:

	#Initialise UDP Listener
	def __init__(self, host='0.0.0.0', port=5005, buffer_size=1024):

		self.host = host
		self.port = port
		self.buffer_size = buffer_size
		self.running = False
		self.callback = None

	# Start Function
	def start(self):

		self.running = True
		threading.Thread(target=self._listen, daemon=True).start()

	# Stop Function
	def stop(self):

		self.running = False

	# Listen/Handle UDP Packets
	def _listen(self):

		with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
			server.bind((self.host, self.port))
			print(f"UDP Listener started on {self.host}:{self.port}")
			while self.running:
				try:
					data, address = server.recvfrom(self.buffer_size)

					payload = json.loads(data.decode())

					print(
						f"Received data: from {address}")

					print(payload)

					requests.post(
						"http://localhost:5000/api/telemetry",
						json=payload
					)

					if self.callback:
						self.callback(payload())
				except Exception as e:
					print(f"Error receiving data: {e}")
			print("UDP Listener Stopped")

# Main loop
if __name__ == "__main__":

	# Example usage
	def handle_data(data):
		print(f"Processing telemetry: {data}")

	listener = SensorListen(port=5005)
	listener.callback=handle_data
	listener.start()

	try:
		while True:
			sleep(1)  # Keep main thread alive
	except KeyboardInterrupt:
		listener.stop()

