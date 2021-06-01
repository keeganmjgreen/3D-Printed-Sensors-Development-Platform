# Example Data Sheets #

This document will serve as a compendium of sensor and evaluation boards Data Sheets and User Manuals. 
Documentation will be gathered from multiple vendors, configurations (module or evaluation board) and sensor type (strain, accelerometer or environmental).
The document will conclude with an analysis of common content, structure and conventions between user manuals as well as their core differences.

## Strain Gauges ##

### Evaluation Boards ###

[HX711 Load Cell - Data Sheet](https://cdn.sparkfun.com/assets/b/f/5/a/e/hx711F_EN.pdf)

[LTC2483 Demonstration Boad (Strain & temperature) - User Manual](https://www.analog.com/media/en/technical-documentation/user-guides/dc955af.pdf)

### Sensor Modules ###

[OMEGA Transducer Quality Strain Gauge - Data Sheet](https://assets.omega.com/pdf/test-and-measurement-equipment/strain-gauges/SGT_UNIAXIAL.pdf)

## Accelerometers ##

### Evaluation Boards ###

[ADXL377 Evaluation Board - User Manual](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-analog-accelerometer-breakouts.pdf)

### Sensor Modules ###

[ADXL335 (3-axis) - Data Sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL335.pdf)

[ADXL312 (3-axis) - Data Sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL312.pdf)

## Environmental Sensors ###

### Evaluation Boards ###

[DFR0067 - User Manual](https://www.digikey.ca/htmldatasheets/production/2071184/0/0/1/dht11-humidity-temp-sensor.html)

### Sensor Modules ###

[DFR0067 - Data Sheet](http://image.dfrobot.com/image/data/DFR0067/DFR0067_DS_10_en.pdf)

### Data Logging Devices ###
[RHTEMP101A - User Manual](https://www.madgetech.com/wp-content/uploads/2020/05/rhtemp101a-pug.pdf)


## Notes & Conclusions ##

There is a large degree of variation between sensor Data Sheets/User Manuals. Different manufacturers and suppliers have markedly different scope and organization of data included. Evaluation boards tend to have much more information, specifically with regard in how to calibrate and use the sensor compared to individual sensor modules. This difference is even reflected within the document name - Evaluation Boards are more likely to have User Manuals and modules are more likely to have Data Sheets. Pithon is more akin to an evaluation board than a module. 

Common Headings and information contained in sensor User Manuals that are relevant to Pithon are:

- Product Description
  - 1/3 to 1/2 page description of the product
  - Summary of key features/selling points
  - Link to manufacturer's website for additional info and demosntrations
- System Diagram
  - Non-technical (usually) system level diagram, sometimes with a scale reference. Either physical system or computer model.
- Quick Start Guide
  - Essentially just a description on how to use the product as fast as safely possible.
- Installation/Hardware Setup
  - How to properly setup the device into normal operating conditions. Always follows the Quick Start Guide
- Calibration
  - Sometimes called 'Experiments'
  - Detailed description on how to calibrate the device.
  - Seperated into multiple subheadings for testing each individual part of the calibration process 
- Source Code (In some manuals)
  - Snippets of source code that can be used to utilize the sensor to its fullest extent.
- Specifications
  - All the technical information for the sensor such as bandwidth, sensitivity, max input voltage/current, etc. 
- Circuit Diagram (Schematic Diagram)
  - Always only one system level circuit diagram including all wiring.
- Legal Notice
  - All relevant legal information/waivers, essentially to explain to not take a bath with your accelerometer.
