
# RPi_IOT_Application_Proposal

## Chloe Croydon 20119102

Repository: https://github.com/ChloeKC/IOT_Application_RPi
#

![RPI](image-3.png)
#

## Introduction

### Smart Home - Climate Analysis and Alerts

IoT device monitors environmental conditions and Raspberry Pi processes data locally. IoT platform publishes collected data and insights via UI apps and notification systems. Utilizes event-driven architecture to provide real-time alerts via push notifications when conditions go outside an optimal, predefined threshold. 

##### “Build Tight, Ventilate Right.” SEAI

A cost saving, health and environment friendly solution for air quality and temperature regulation in a fully insulated, airtight environment without adequate mechanical ventilation and heat recovery. Monitoring and solving consequent temperature,  moisture and mould issues, with further possibilities for excess VOC, CO2 and Radon detection.

![Retrofit_Dublin](image-8.png)

## Tools, Technologies and Equipment

### Raspberry Pi: 
Linux based RPi OS and systemd. 

### Sense HAT:
Monitors temperature and humidity and notifies user visually, with LED indicators, when values fall outside optimal range. Displays red for too hot or humid and blue for too cold or humidity below 40%.

### Python over SSH: 
Python script processes data collected from RPi, then securely forwards data in Json files to MQTT broker/platform, which publishes information to subscribers.

### Blynk: 
EDA alerts user remotely via web dashboard and mobile app. It reliably filters, aggregates and live streams transformed data as visual information/statistics to users without the need for middleware (decoupled design).

### Smart Plug:
Possibilities for remote climate control and intuitive home automation.

### MongoDB Compass:
Chosen database for logging live climate IoT data, with flexibility to handle and scalability to manage high-velocity data collection. No pre-defined schemas for storing diverse data from multiple sources.

### HTML:
Possibilities for adding live, home climate conditions to the Whether Weather App, indoor/outdoor comparisons.

![alt text](image-9.png)

### Testing: 
Rpi and Sense HAT setup in downstairs bedroom collecting cumulative data to test the quality of python processing code, information gathering technique and published alerts and insights. 
Potential for use of simulated data with temperature/humidity spikes and troughs for alert system. Statistical analysis of home air quality including comparative study with optimal living conditions. Useful for predictive model training for intuitive home assistant.



