# Pithon Software

The software that has been developed as part of the Pithon platform as well as how you may use it will both be discussed. This is important because providing a breakdown of Pithon software by functionality is integral to realizing all of the testing, calibration, evaluation, and end use of Pithon sensors. All of the following C++/Arduino language and Python software were in the development of the Pithon platform for 3D printed sensors.

## C++/Arduino Language

A set of C++/Arduino programming language codes has been assembled. They span the tasks of isolating sensor resistance from its basic interface circuit, to relaying this data to your computer (over serial communication) for real-time monitoring, real-time plotting, and sensor calibration. After the interactive calibration process, automatically generated calibration code -- which defines a model of your sensor behavior -- converts the sensor response to the measurand. Signal processing and/or filtering is further implemented. The Arduino codes may also be used to:

 1. Implement an AC voltage source through onboard pulse-width modulation to run a Pithon environmental sensor,
    
    and

 2. Isolate its responses to environmental conditions while reading from a commercial environmental sensor in order to calibrate your own one.

Some of our microcontroller codes can be found [here](https://3d-printed-sensors-development-platform.readthedocs.io/en/latest/4-Terminal-Sensing-for-Real-Time-Data-Logging-Using-a-Microcontroller.html).

## Python

An open-source collection of simple-yet-effective and customizable software tools have been custom-made in the easy-to-use Python programming language. Choosing Python was a conscious decision for speed, accessibility, straightforward data manipulation and aggregation, and to suit the sensible needs of the open-source community.

**Microcontroller-Based Analog Data Logger Interface**

A Windows 10 interface for a microcontroller-based analog data logger with a wired conection to a computer has been developed to help you get up and running with your microcontroller and save/visualize its transmitted data. This timeseries data may be a sensor resistance measured by their microcontroller, or a calibrated measurement determined therefrom. The interface prompts you to connect your microcontroller (via USB) if it has not already been connected, notifies that the device was connected, reads from the device in real time over serial communication, and finally notifies that the device was disconnected. It then prepares the collected analog data. Most importantly, however, it makes the results accessible through a CSV file generated in the working directory as well as an interactive, in-browser plot with export options. This can help you calibrate, test, and troubleshoot your sensor setup.

![](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/img/Microcontroller_Based_Analog_Data_Logger_Interface_Example.png)

The technical documentation of the microcontroller-based analog data logger interface is available [here](https://3d-printed-sensors-development-platform.readthedocs.io/en/latest/Microcontroller-Based-Analog-Data-Logger-Interface.html). \
​

Furthermore, Windows interfaces for collecting, preparing, and processing your force sensor calibration data has been developed to assist you in the calibration process. An older version of the calibration process before it was automated can be found [here](https://3d-printed-sensors-development-platform.readthedocs.io/en/latest/Calibrating-Your-Force-Sensor.html).

[**Pithon Data Collection Software**](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/Force-Sensor-Calibration-Software/Force-Sensor-Calibration-Data-Collection/Force_Sensor_Calibration_Data_Collection.py)

Like the above interface, Pithon data collection software also establishes a communication link between your computer and microcontroller. Its main purpose is to assist you thereafter during the hands-on calibration step of collecting your raw sensor data, while recording how it was done for future reference.

![](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/img/Pithon-Software/Force_Sensor_Calibration_Data_Collection.png) \
$\uparrow$ The command-line interface of Pithon force sensor calibration data collection software.

What this interface does is tedious to do using the Arduino Serial Monitor or similar. Moreover, a technical limitation observed of serial communication with the Arduino limits the stable data transfer speed in this context to a fraction of what it otherwise would be, meaning that so would be the sample rate of the sensor response. The highest possible/stable sample rate is desired to compensate for measurement noise.

[**Pithon Data Preparation Software**](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/Force-Sensor-Calibration-Software/Force-Sensor-Calibration-Data-Preparation/Force_Sensor_Calibration_Data_Preparation.py)

Pithon data preparation software organizes your collected data, summarizes the calibration process with statistics, and allows you to assess and verify the behavior of your sensors visually. This software tool does what would take hours to do in Excel as a painstaking manual data preparation process.

![](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/img/Pithon-Software/Force_Sensor_Calibration_Data_Preparation.png) \
$\uparrow$ The command-line interface of Pithon force sensor calibration data preparation software.

The sensor response samples are aggregated to eliminate the effect of measurement noise. To this end, the number of samples, the mean, and the statistical variance are all reported for each calibration segment. In the most recent version, a measure of sensor drift over time and the variance after accounting for sensor drift are also reported. In addition, a 'partitioned' timeseries plot of the sensor response over the course of the calibration process is generated, which you can conveniently save for future reference.

[**Pithon Data Processing Software**](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/Force-Sensor-Calibration-Software/Force-Sensor-Calibration-Data-Processing/Force_Sensor_Calibration_Data_Processing.py)

Pithon data processing software generates a calibration curve to model the behavior of your sensors, along with its microcontroller code.

![](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/img/Pithon-Software/Force_Sensor_Calibration_Data_Processing.png) \
$\uparrow$ The command-line interface of Pithon force sensor calibration data processing software.

A curve fit is performed on the aggregated data points that are generated by the previous interface. The curve delineates the maximum and minimum sensitivity values across the measurement range for which the sensor is calibrated, which are also reported in our most recent version as important sensor specifications. For the Pithon environmental sensor, the curve fit becomes a surface fit for each of temperature and humidity outputs. The software tool is set up to use polynomial-based curves, arbitrary mathematical functions, or even machine learning regressors (such as linear, nonlinear, decision tree, etc.) for its calibration models. The simplest model that effectively describes the data is to be used and its C++ code is automatically generated to be implemented on your microcontroller -- which is also used for signal processing. \
​

This completes the completes the Pithon calibration software process:

![](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/img/Pithon-Software/Pithon-Calibration-Software-Process.svg)

----
