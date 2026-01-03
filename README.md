# RaspPi Fitness System

**This was A-Level examined work created years ago, copying this as another student will likely lead to being flagged for plagiarism!**\
Desktop utility designed to tackle a rising issue to do with lack of fitness in today's society. Allows users to track their nutrition which is visualised in graphs, running progress via hardware sensors and more.

## Overview

This project has a comprehensive GUI that integrates with the Raspberry Pi's sense hat and camera modules. Detailed graphing and user-friendly inputs provide space for the user to track their steps and speed in real-time and scan food items for caloric data which they then can input into their calorie tracker. There is also a gamification feature that provides the user with progressive challenges.

## Features

* **Live Activity**:
    * **Real-Time Tracking**: Uses the sense hat module's accelerometer to calculate steps, current speed and uses those as input to the calorie algorithm
    * **Calorie Algorithm**: Calculates calories burned based on METs (Metabolic Equivalent of Task), user BMR and movement intensity
    * **Personalised Calibration**: People are different, some shake more when stationary so I made a calibration phase before the user starts to run to adjust the sensor's sensitivity and noise handling to properly detect when they are moving
* **Nutrition & Scanning**:
    * **Barcode Scanner**: Integrates OpenCV and pyzbar to read food barcodes via the camera and fetch energy values in kcal from API
    * **Manual Search**: If the user doesn't have a camera or doesn't want to use it, then they may manually lookup via product name or barcode ID
* **Security**: User data is securely encrypted using Fernet encryption and passwords are hashed (and salted to avoid birthday attacks) using Bcrypt
* **Visualisation**: Graphs are used to plot weight, calorie intake and activity metrics via Matplotlib
* **Challenges**: Generates challenges of which difficulty incrementally goes up upon completion

## Prerequisites

* **Operating System**: Raspberry Pi *or Windows (note: unable to utilise run tracker)*
* **Runtime**: Python 3.x
* **Libraries**: `SenseHat` (make sure your Raspberry Pi has this), `Tkinter`, `Matplotlib`, `OpenCV`, `pyzbar`, `cryptography`, `bcrypt`, `requests`, `numpy`

## Quick Start

There are two versions of this project, the actual one was intended for the Raspberry Pi to allow the use of its built in accelerometer but I understand it's not the most common piece of hardware to have in hand so I made a windows version that generates random values for the run tracker.\
If you want to run either one, just run the corresponding main.py/pyw file.\
**Note: I used my own API key for a food database, you may need to provide your own if it expires/has expired.**
