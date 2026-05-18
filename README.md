
# RPi_IOT_Application

## Chloe Croydon 20119102

Repository: https://github.com/ChloeKC/healthyhome

Project Folder:cd ~/healthyhome source .venv/bin/activate




![RPi](image-3.png)

### "Healthy Home" - Smart Environment Analysis and Alert System

## Introduction


This project implements an IoT-based indoor climate monitoring system using a Raspberry Pi and Sense HAT. The device collects temperature and humidity data at regular intervals, applies threshold-based logic to classify environmental conditions, and publishes structured JSON messages via MQTT. A cloud-based dashboard visualises the data and provides real-time alerts when conditions fall outside optimal ranges. The project demonstrates edge processing, network communication, and user-facing visuals within an event-driven IoT system. Utilizing user-friendly system architecture and protocols to establish accessibility, security and the separation of concerns:

#### [Sensors] → [Edge Processing] → [MQTT] → [Backend / Logging / Analytics Dashboard] → [User Apps]


####   [Sense HAT] → [Raspberry Pi] → [SSH/Blynk]     →     [Blynk Dashboard]     →     [Mobile Interfaces]


A cost saving, health and environment friendly solution for air quality and temperature regulation in a fully insulated, airtight environment without adequate mechanical ventilation and heat recovery. Monitoring and solving consequent air temperature, pressure, moisture and mould issues, with further possibilities for excess VOC, CO2 and Radon detection. 

‘Airtight houses experience negative pressure, which could reduce airflow’ A. Bailes III. 
This could lead to back drafting where combustion gases, from cooker hoods for example, are pulled back into the house.

![retrofitDublin](image.png)

##### “Build Tight, Ventilate Right.” SEAI

The Sense HAT(IoT device) monitors environmental conditions and the Raspberry Pi(MQTT Client) processes data locally with Python scripting. The collected data is forwarded to Blynk (MQTT Broker) who publishes the processed telemetry and insights via subscribed UI apps(web) and notification systems(smartphone, email). Utilizes event-driven architecture to provide real-time alerts via push notifications when conditions go outside an optimal, predefined threshold.


## Tools, Technologies and Equipment
An edge IoT device monitors indoor climate and sends structured data to a service, which processes it and provides alerts and a dashboard.

### Sense HAT:
Monitors temperature and humidity and notifies user visually, with LED indicators, when values fall outside optimal range. Displays red for hot or high humidity and blue for cold or low humidity.

### Raspberry Pi:
RPi OS. Debian based, Linux distribution, reads sensor values every minute.

### Home Network:
Connected devices communicate and share resources, including computers, smartphones, tablets, Rpi, sensors and other smart devices.

### Python over SSH:
Python script processes data collected from RPi, checks if it's within normal range and logs it. Then securely forwards data in Json files to Blynk/MQTT platform, which alerts and publishes telemetry to subscribers.

### MQTT Broker/Blynk:
EDA alerts user remotely via web dashboard and mobile app. It reliably filters, aggregates and live streams transformed data as visual information/statistics to users(decoupled design). Ensures reliable and efficient data transport with Last Will & Testament LWT feature.

### Write to file:
Log live climate IoT data, storing diverse data from multiple sources.

### Packet Tracer PT:
Simulate scenarios that are difficult to create: Extreme environmental conditions. Update PT sensor to send telemetry data using bridging module. Develop sensor module on RPi that listens for UDP from PT sensor.

### Smart Plugs:
Remote climate control and intuitive home automation.

### HTML:
Future potential for adding live, home climate conditions to the Whether Weather App, indoor/outdoor comparisons.


## Network Topology

![PacketTracer](image-2.png)


## Testing & Data Analysis:


Packet Tracer prototype to simulate a smart home network that utilize IoT devices and applications.

RPi and Sense HAT setup in living space, collecting cumulative data to test the quality of python processing code, information gathering technique and published alerts and insights.

Blynk event and automation testing with simulated data, temperature/humidity spikes/troughs, for tracking events and alerts system.

Statistical analysis of home air quality including comparative study with optimal living conditions. Useful for predictive model training for intuitive home assistant.

![Topology](image-1.png)

## Project Graphic:

Project idea, proposal, and approval
Get input/data source working on the Raspberry Pi
Implement networking/connection with other component/platform/service
Add output layer such as dashboard, logging, alerts, or storage Week5
Testing, refinement, documentation, GitHub cleanup, and demo preparation

![Graphic](image-4.png)

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

## Marking Guide

Release 1(Core) 
• At least one sensor or simulated data source (e.g. temperature, button, motion, External API). 
• Regular data collection. 
• Some local processing of raw values (e.g. thresholds, states, simple rules). 
• One running program that shows behaviour clearly (console output acceptable). 
• Basic logging/display (print values, write to file, simple terminal UI). 
• Clear project description: problem, aim, and what you're building. 

Release 1 Base (30-49) 
One input source to Device Physical/Data link layer solution. Basic one way connection between device/processes. 2 programme strands present in output. Basic knowledge of each exhibited. (e.g. programming, database, computer systems) Zip file and/or basic Repo: Minimal (1) communication resource used (e.g.simple readme.md) and video. 


Release 2(Good) 
• Two distinct components/processes (e.g. sensor/edge node + service/dashboard). 
• At least one network connection (MQTT, API, TCP/UDP, HTTP). 
• Structured data messages (JSON recommended). 
• Meaningful data handling beyond raw logging (averages, states, or simple analytics). 
• Basic dashboard or visualisation (web page, terminal UI, or simple graph). 
• Initial architecture diagram (boxes + arrows is fine). 
Edge device sends JSON readings to a second service via MQTT/HTTP. The service logs the messages and shows a simple dashboard page.
Release 2 Good (50-64)
 At least one real or simulated input source Wireless/Wired protocols  including network and transport layer. Interconnected device(s) and or processes. Apply and combine concepts from more than two modules/strands.. Good GithubRep: Repository includes clearstructure, documentation. 


