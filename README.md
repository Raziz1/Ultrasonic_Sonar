# Ultrasonic_Sonar 🔊📡
Creating a sonar device using a HC-04 ultrasonic sensor on the Raspberry PI

## Parts 🛠
* [Raspberry Pi 4 Model B](https://www.amazon.ca/Raspberry-Pi-Computer-Model-4GB/dp/B07W4JM192/ref=sr_1_7?dchild=1&keywords=raspberry+pi+4&qid=1607186145&sr=8-7)
* [HC-04 Ultrasonic Sensor](https://www.amazon.ca/Sainsmart-HC-SR04-Ranging-Detector-Distance/dp/B004U8TOE6/ref=sr_1_2?dchild=1&keywords=ultrasonic+sensor+hc-04&qid=1613609674&sr=8-2)
* [SG90 Micro-Servo](https://www.amazon.ca/Miuzei-Helicopter-Airplane-Remote-Controls/dp/B07Z16DWGW/ref=sr_1_2_sspa?dchild=1&keywords=sg90+servo&qid=1613609758&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNTMyTzRTWFc0R05aJmVuY3J5cHRlZElkPUEwODc5NzYxMzVSNVdNQ1NVR1owOCZlbmNyeXB0ZWRBZElkPUEwODI3NzczNUQyVkxHQkRSSlBMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)

## Libraries 📚
* [RPI.GPIO](https://pypi.org/project/RPi.GPIO/)
* Time
* Math
* [pygame](https://pypi.org/project/pygame/)

## Overview
* This project creates a ultrasonic sonar device that can scan an area within 180 degrees of motion. 
* The ultrasonic sensor emits a low a sound puls and receives the resulting output pulse. The output pulses width determines the distance it travelled. 
* In our case it stores 15 distance values across 180 degrees and plots them on a "sonar graph" in relation to its position.
* For more information and the datasheets on the SG90 servo you can visit [components101 servo](https://components101.com/servo-motor-basics-pinout-datasheet)
* For more information and the datasheets on the HC-04 Ultrasonic Sensor you can visit [components101 ultrasonic sensor](https://components101.com/ultrasonic-sensor-working-pinout-datasheet)
* This project can also be done using an Arduino board as well as the Processing library to graphically display the information


## Schematics ⚡

### SG90 Micro-Servo Wiring
|   **Raspberry PI Board**  | **GPIO Extension Board** | **SG90 Micro-Servo**|
| ------------- |:-------------:|:-------------:|
| 5V            | 5V            | 5V (Red)      | 
| Ground        | Ground        | Ground (Black)|   
| GPIO6         | GPIO25        | PWM (Orange)  | 

### HC-04 Ultrasonic Sensor Wiring
|   **Raspberry PI Board**  | **GPIO Extension Board** | **HC-04 Ultrasonic Sensor**|
| ------------- |:-------------:|:-------------:|
| 5V            | 5V            | 5V            | 
| Ground        | Ground        | Ground        |   
| GPIO0         | GPIO17        | Trig          | 
| GPIO1         | GPIO18        | Echo          | 
