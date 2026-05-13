
# RPi_IOT_Application

## Chloe Croydon 20119102

Repository: https://github.com/ChloeKC/healthyhome
#
Project Folder:cd ~/healthyhome source .venv/bin/activate
#

![RPi](image-3.png)
#

## Introduction


### "Healthy Home" - Smart Environment Analysis and Alert System

This project implements an IoT-based indoor climate monitoring system using a Raspberry Pi and Sense HAT. The device collects temperature and humidity data at regular intervals, applies threshold-based logic to classify environmental conditions, and publishes structured JSON messages via MQTT. A cloud-based dashboard (Blynk) visualises the data and provides real-time alerts when conditions fall outside optimal ranges. The project demonstrates edge processing, network communication, and user-facing visuals within an event-driven IoT system.

#### [Sensors] → [Edge Processing] → [MQTT] → [Backend / Logging / Analytics Dashboard] → [User Apps]

####   [Sense HAT] → [Raspberry Pi] → [MQTT]     →     [Blynk Dashboard]     →     [User Interfaces]

##### “Build Tight, Ventilate Right.” SEAI

A cost saving, health and environment friendly solution for air quality and temperature regulation in a fully insulated, airtight environment without adequate mechanical ventilation and heat recovery. Monitoring and solving consequent temperature, moisture and mould issues, with further possibilities for excess VOC, CO2 and Radon detection. 

A "too tight" home can cause negative pressure, leading to backdrafting, where combustion gases are pulled back into the house. 

![Retrofit_Dublin](image-8.png)

Utilizing user-friendly system architecture and protocols to establish scalability, security and the separation of concerns. The Sense HAT(IoT device) monitors environmental conditions and the Raspberry Pi(MQTT Client) processes data locally with Python scripting. The collected data is forwarded to Blynk (MQTT Broker) who publishes the processed telemetry and insights via subscribed UI apps(web) and notification systems(smartphone, email). Utilizes event-driven architecture to provide real-time alerts via push notifications when conditions go outside an optimal, predefined threshold.

			[Sense HAT]
			↓
		[Raspberry Pi]
			↓
			[Blynk MQTT Broker]
			↓ 
		[Blynk Dashboard]
			↓
			[Blynk User App & Alerts]


## Tools, Technologies and Equipment
An edge IoT device monitors indoor climate and sends structured data to a service, which processes it and provides alerts and a dashboard.

### Sense HAT:
Monitors temperature and humidity and notifies user visually, with LED indicators, when values fall outside optimal range. Displays red for hot or high humidity and blue for cold or low humidity

### Raspberry Pi:
RPi OS. Debian based, Linux distribution.

### Home Network:
Connected devices communicate and share resources includes computers, smartphones, tablets, Rpi, sensors and other smart devices.

### Python over SSH:
Python script processes data collected from RPi, then securely forwards data in Json files to MQTT broker/platform, which publishes information to subscribers.

### Raspberry Pi: 
RPi OS, Debian based Linux distribution.

### Home Network:
Connected devices communicate and share resources includes computers, smartphones, tablets, Rpi, sensors and other smart devices

### Python over SSH: 
Python script processes data collected from RPi, then securely forwards data in Json files to MQTT broker/platform, which publishes information to subscribers.

### MQTT Broker Blynk:
EDA alerts user remotely via web dashboard and mobile app. It reliably filters, aggregates and live streams transformed data as visual information/statistics to users(decoupled design). Ensures reliable and efficient data transport with Last Will & Testament LWT feature.

                           [Sense HAT Sensors]
                                    ↓
                    [Raspberry Pi (Edge Processing)]
                                    ↓
                              [MQTT Broker]
                                    ↓ 
                 [Blynk] [Backend / Logging / Analytics]
                                    ↓
                        [User Dashboard & Alerts]

### Packet Tracer PT:
Simulate scenarios that are difficult to create: Extreme environmental conditions. Update PT sensors to send data via UDP using bridging module. Develop a sensor module on RPi that “listens” for PT sensor data.

### Smart Plugs:
Remote climate control and intuitive home automation.

### Write to file:
Log live climate IoT data, storing diverse data from multiple sources.

### HTML:
Possibilities for adding live, home climate conditions to the Whether Weather App, indoor/outdoor comparisons.

### Packet Tracer PT:
Simulate scenarios that are difficult to create: Extreme environmental conditions. Update PT sensors to send data via UDP using bridging module. Develop a sensor module on RPi that “listens” for PT sensor data.

## Network Topology

![Topology](image-9.png)


## Testing & Data Analysis:
Packet Tracer prototype to simulate a smart home network that utilize IoT devices and applications.
RPi and Sense HAT setup in living space, collecting cumulative data to test the quality of python processing code, information gathering technique and published alerts and insights. 
Potential for use of simulated data with temperature/humidity spikes/troughs for alert system.
Statistical analysis of home air quality including comparative study with optimal living conditions. Useful for predictive model training for intuitive home assistant.


## Project Graphic:


![Graphic](image.png)

## Findings:
The SenseHAT is good at measuring local environment, not a reliable
 measure of the air temp and humidity in the room. 
Offset neccessary or calibrate data against a reliable measurement device.
	## humidity = humdty * (2.5 - 0.029 * temp)
The humidity sensor on the SenseHAT generally reads too low 
because it is affected by heat from RPi CPU.
Or an adapter to seperate HAT from RPi. Or infrequent readings.
Display layer introduces delays during LED message rendering.
Git commits are difficult pull, conflict, resolve, rebase, push!
	
	## humidity = humdty * (2.5 - 0.029 * temp)
