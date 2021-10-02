[Download as PDF](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/pdf/Overview.pdf)

----

# About This Manual #

This manual describes every aspect of the Pithon platform including how to customize, print, calibrate and use Pithon sensors. The manual starts with an overview of Pithon sensors. Next, the process of 3D printing sensors will be described, emphasizing strategies for improving reliability and consistency of printed sensors. Tools and resources for customizing sensors to your unique application will then be presented. Finally, calibration methods are provided to ensure that printed sensors are delivering reliable results. 

# Overview #

Pithon is a set of designs, tools, documentation, and software to allow anyone to customize and 3D print their own sensors. Monti 3D Printing Solutions currently offers support for temperature sensors, force sensors, and accelerometers. We are currently developing designs for a humidity sensor, environmental sensor which can measure temperature and humidity simultaneously, and a magnetic field sensor. These sensors should be released by the end of August 2021. Pithon is a fully modular embedded sensor platform wherein users can select which sensors and functionality they require, modify sensor designs to their unique application, and easily embed their sensors into any structure. The image below displays example Pithon sensors. 

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/img/Overview/Pithon-Overview.png" alt="Pithon Overview" style="zoom:25%;" />

Using only 2 materials, a conductive and a structural 3D printing filament, Pithon sensors can be 3D printed in a single-step manufacturing process. After the sensors are produced, users can choose whether to perform additional steps to improve sensor performance, such as adding a metal proof mass to improve an accelerometer's sensitivity. Complete sensors can be printed for about $1 CAD in an hour. 

## Temperature Sensor ##

Pithon's temperature sensor features a small, but robust design. A protective covering, or shroud, protects the sensor in case an impact occurs. The sensor's small design allows for a rapid response to variations in temperature, making it ideal for applications that involve rapid heating and cooling cycles. This sensor is very sensitive to variations in temperature, its resistance increases ~1.5 times when the sensor is heated to 50 °C.

## Force Sensor ##

Our force sensor is a comprehensive design, automatically correcting force measurements for variations in environmental conditions, such as temperature. The force sensor consists of conductive traces along a cantilever beam. When a mass, or force, is applied to the free end of the beam, the beam will bend causing the conductive traces to either expand or compress, thereby changing their resistance. An optional Compensating Element is included that provides automatic compensation for variations in environmental conditions.


## Accelerometer ##

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/img/Overview/Accelerometer-Design.png" alt="Accelerometer Design" style="zoom:25%;" />

Pithon's accelerometer is similar in design to our force sensor. Users have the option of installing a metal ball in the accelerometer to improve its sensitivity. The ball is installed in a single-step process by pressing the ball into its corresponding hole. Monti 3D Printing Solutions is actively characterizing the performance of our accelerometers and will update this description with performance characteristics shortly.   

----
