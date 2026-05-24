
# RPi_IOT_Application

## Chloe Croydon 20119102

Repository: https://github.com/ChloeKC/healthyhome

Project Folder: cd ~/healthyhome source .venv/bin/activate

![RPi](image-3.png)

### "Healthy Home" - Smart Environment Analysis and Alert System


### Healthy Home files:

script.py
backend_api.py
sense_listen.py
render.html
telemetry.json
blynk.py
blynk_pt.py
healthyhome.pkt
README.md

## Introduction

This project implements an IoT-based indoor climate monitoring system using a Raspberry Pi and Sense HAT. The device collects temperature and humidity data at regular intervals, applies threshold-based logic to classify environmental conditions. The information is stored and published as structured JSON messages via MQTT and HTTP applications. A cloud-based dashboard visualises the data and provides real-time alerts when conditions fall outside optimal ranges. The project demonstrates edge processing, network communication, and user-facing visuals within an event-driven IoT system. Utilizing user-friendly system architecture and protocols to establish accessibility, security and the separation of concerns:

####   Sensors → Edge Processing → UDP Simulation → HTML/MQTT → Backend API → Dashboard Service → User Apps

####   Sense HAT →  RPi/Python →  Flask/Render/Blynk → Packet Tracer → Blynk Dashboard → Mobile Interfaces


A cost saving, health and environment friendly solution for air quality and temperature regulation in a fully insulated, airtight environment without adequate mechanical ventilation and heat recovery. Monitoring and solving consequent air temperature, pressure, moisture and mould issues, with further possibilities for excess VOC, CO2 and Radon detection. 
‘Airtight houses experience negative pressure, which could reduce airflow’ A. Bailes III. This could lead to back drafting where combustion gases, from cooker hoods for example, are pulled back into the house.

‘Airtight houses experience negative pressure, which could reduce airflow’ 
								A. Bailes III. 
This could lead to back drafting where combustion gases, a cooker hood for 
example, are pulled back into the house.

![Retrofit_Dublin](image-8.png)

##### “Build Tight, Ventilate Right.” SEAI

The Sense HAT(IoT device) monitors environmental conditions and the Raspberry Pi(MQTT Client) processes data locally with Python scripting. The collected data is forwarded to Blynk (MQTT Broker) who publishes the processed telemetry and insights via subscribed UI apps(web) and notification systems(smartphone, email). Utilizes event-driven architecture to provide real-time alerts via push notifications when conditions go outside an optimal, predefined threshold.

#### Ventilation 	Mould Prevention 	Thermal Comfort	Smart/Remote Control

####     Indoor Environment Monitoring 	Future VOC / CO₂ / Radon Sensing


## Project Graphic:

![Graphic](image-5.png)

## Tools, Technologies and Equipment
An edge IoT device monitors indoor climate and sends structured data to a service, 
which processes it and provides alerts and a dashboard.


Sense HAT          Packet Tracer UDP
     ↓                   ↓    
     sensor_service.py
               ↓	  HTTP POST JSON	
     udp_listener.py
               ↓
     Flask Backend API
               ↓
          Telemetry .JSON
               ↓
     Blynk Dashboard / API

### Sense HAT:
Monitors temperature and humidity and notifies user visually, with LED indicators, 
when values fall outside optimal range. Displays red for hot or high humidity and 
blue for cold or low humidity.

### Raspberry Pi:
RPi OS. Debian based, Linux distribution, reads sensor values at regular intervals.

### Home Network:
Connected devices communicate and share resources, including computers, smartphones, 
tablets, Rpi, sensors and other smart devices.

### Python over SSH:
Python script processes data collected from RPi, checks if it's within normal range and 
logs it. Then securely forwards data in Json files to Blynk/MQTT dashboard, which 
publishes telemetry to subscribers with alerts and storage.

### MQTT Broker/Blynk:
EDA alerts user remotely via web dashboard and mobile app. It reliably filters, aggregates 
and streams transformed data as visual information/statistics to users (decoupled design). 
Ensures reliable and efficient data transport with Last Will & Testament LWT feature.

### Flask/Storage:
Backend system for data ingestion/storage, potential to handle diverse data from multiple IOT.

### HTML:
GET & POST methods for data retrieval and server delivery, stored in the request body of HTTP request for securely logging and displaying live home climate conditions to Flask Web API. 

### Github:
GitHub commits for project development documentation.

### Smart Plugs:
Remote climate control and intuitive home automation.

### Demonstration:
Youtube video/demo.

### Packet Tracer / Digital Twin:
Simulates scenarios that are difficult to create for testing. Update PT sensor to send 
telemetry data using bridging module. Develop sensor module on RPi that listens for UDP's 
from PT sensor.

## Network Topology/Prototyping

![PacketTracer](image-2.png)

### Simple Home Network in Packet Tracer:
Configured Network Devices
Simulated IoT/Senser Devices
Telemetry Ingestion 
UDP transport Protocol
Sensor Listener
Threaded Network
Packet Handling
Blynk Integration

![Topology](image-1.png)

## Testing & Data Analysis:

RPi and Sense HAT setup in living space, collecting cumulative data to test the quality of python processing code, information gathering technique and published alerts and insights.

Blynk event and automation testing with simulated data, temperature/humidity spikes/troughs, for tracking events and alerts system.

Packet Tracer prototype to simulate a smart home network that utilize IoT devices and apps.

Statistical analysis of home air quality i.e. comparative study with optimal temperature values. Useful for predictive model training for intuitive home assistant with smart hardware.


## Problems/Findings:

The temperature sensor on the SenseHAT generally reads too high as it is affected by heat from RPi CPU.
The humidity sensor generally reads too low because it is also affected by heat.
Display layer introduces delays during LED message rendering. 
Git commits difficult: pull, conflict, resolve, rebase, push.


### Solutions:

An adapter to separate HAT from RPi.
Offset by 20% for air temperature and humidity values in the room.
Calibrate data against a reliable measurement device essential.
Infrequent readings. 

### Conclusions:
The humidity was constantly too low in our home.
The SenseHAT is good at measuring local environment, not a reliable measure of the air temp and humidity in the room. 
