# Azure-IoT-Edge-Demo

This repo contains Azure IoT Edge Demos:

1. Edge Offset Demo
....

More under developing


### Edge Offset Demo
This demo will get data from SimulatedTemperatureSensor and output to Azure IoT Hub, with functions:
- When detect a machine temperature over TEMPERATURE_THRESHOLD, add property Alert to message then output to IoT Hub, original function from Azure IoT Edge Demo
- Modify the original temperature data from SimulatedTemperatureSensor and plus/minus a offset then output to IoT Hub

In module tiwn you can esaily change the value of:
- TemeratureThreshold,
- EncodedOffset,
- EncodedSwitch
