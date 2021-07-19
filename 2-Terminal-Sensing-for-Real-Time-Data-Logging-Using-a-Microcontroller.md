# 2-Terminal Sensing for Real-Time Data Logging Using a Microcontroller

2-terminal sensing is less consistent between sensors and less repeatable for a given sensor than 4-terminal sensing. However, it is simpler to get up and running, and more compact in implementation.

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/2-Terminal-Sensing-for-Real-Time-Data-Logging-Using-a-Microcontroller.png" style="zoom:50%;" />

$\uparrow$ Wiring diagram showing the interface between a sensor with conductive traces for 2-terminal sensing and a microcontroller, of which `A0` -- `A1` are analog input pins. The microcontroller is programmed by and sends data -- namely, the resistance of the conductive traces between the 2 terminals -- to a computer, all via USB over *serial communication*.

## Materials and Preparation

 -  A computer with the [Arduino IDE](https://www.arduino.cc/en/Guide/Environment) (recommended) installed
 -  A microcontroller with at least 1 analog input pin, such as an [Arduino](https://www.arduino.cc/en/Main/Products) (recommended) [Uno](https://www.arduino.cc/en/Main/arduinoBoardUno&gt) or [Nano](https://www.arduino.cc/en/pmwiki.php?n=Main/ArduinoBoardNano), and its USB cable
 -  A sensor with conductive traces for 2-terminal sensing
 -  A 10-kΩ or similar through-hole resistor of known value

**For Testing** and Evaluation Purposes

 -  3 lengths of solid core hook-up wire stripped of its insulation on both ends
 -  3 insulated crocodile clip jumpers (double-ended)

**For Production** without a Circuit Board

 -  3 lengths of solid core hook-up wire stripped of its insulation on both ends
 -  Soldering setup
     -  Soldering iron with stand
     -  Lead-free solder
     -  Soldering sponge or similar
 -  3 pieces of thin heat shrink tubing
 -  2 lengths of thin (e.g., 30 AWG) wire stripped of its insulation on both ends.
 -  Conductive paint syringe
 -  Masking tape

## Instructions -- Assembly

**For Testing** and Evaluation Purposes

 1. Connect your hook-up wires to the `GND`, `A1`, and `5V` pins of your microcontroller.
    
 2. Connect your crocodile clip jumpers to the hook-up wires.
    
 3. Connect your resistor midway through the `A1` wire assembly.
    
 4. Connect the end of the `GND` wire assembly to the resistor.
    
 5. Connect the ends of the remaining wire assemblies, in order, to terminals `T1` -- `T2` of your 2-terminal sensor.

**For Production** without a Circuit Board

 1. Connect your hook-up wires to the `GND`, `A1`, and `5V` pins of your microcontroller. \
    Slip on your heat shrink tubing if necessary at this point.
    
 2. Solder your thin wire to the latter 2 hook-up wires.
    
 3. Solder your resistor midway through the `A1` wire assembly.
    
 4. Solder the `GND` hook-up wire to the resistor.
    
    Apply the heat shrink tubing around all connections by evenly heating it using your soldering iron.
    
 5. Connect the ends of the remaining wire assemblies, in order, to terminals `T1` -- `T2` of your 2-terminal sensor.
    
     1. Coil the stripped ends of your thin wires into loops.
     2. Carefully rest the loops on the center of the matching terminals' contact pads, holding the wires and sensor down using masking tape.
     3. Carefully cover the wire loops with conductive paint within the borders of the contact pads.
     4. Wait for your conductive paint to fully dry/harden.
    
    See also **Using Conductive Paint** and **Preparing Electrical Contacts**.

If you are using an Arduino microcontroller, open its IDE on your computer and plug in your board using its USB cable.

## Instructions -- Programming

If you are using an Arduino microcontroller, upload the following code to it using the its IDE, after which it will begin running onboard.

``` c++
float R_series = 10e3;  // Known value of resistor in series with 2-terminal sensor.

float V_1;

float I;
float V_sens;
float R_sens;

void setup()
{
    Serial.begin(9600);   // Open communication with a computer via USB or with another device via UART.
}
void loop()
{
    V_1 = analogRead(1);  // Measured voltage across series resistor.
    
    I = V_1 / R_series;   // Calculated current through both series resistor and 2-terminal sensor.
    V_sens = 5 - V_1;     // Calculated voltage across 2-terminal sensor.
    R_sens = V_sens / I;  // Calculated resistance of 2-terminal sensor.
    
```

If you are going to use the Arduino *Serial Plotter*, append this code:

``` c++
    Serial.print("R_sens:");
    Serial.print(R_sens);
    Serial.print("\t");
    
    Serial.print("lower:");
    Serial.print(0);
    Serial.print("\t");
    
    Serial.print("upper:");
    Serial.print(10e3);
    Serial.print("\r\n");
}
```

 -  Or download the fully assembled [`2_Terminal_Sensing_for_Real_Time_Data_Logging_Using_Arduino_Serial_Plotter.ino`](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/2_Terminal_Sensing_for_Real_Time_Data_Logging_Using_Arduino_Serial_Plotter.ino).

If you are going to use the Arduino *Serial Monitor*, append this code:

``` c++
    Serial.println(R_sens);
}
```

 -  Or download the fully assembled [`2_Terminal_Sensing_for_Real_Time_Data_Logging_Using_Arduino_Serial_Monitor.ino`](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/2_Terminal_Sensing_for_Real_Time_Data_Logging_Using_Arduino_Serial_Monitor.ino).

### Additional Resources

[Arduino Language Reference](https://www.arduino.cc/reference/)

 -  Communication -- [Serial](https://www.arduino.cc/reference/en/language/functions/communication/serial/)
 -  Analog input/output -- [analogRead()](https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/)

## Real-Time Data Logging

 -  Use the Arduino IDE Serial Plotter ([online reference](https://arduinogetstarted.com/tutorials/arduino-serial-plotter)) to visualize live data over a recent period of time.
 -  Use the Arduino IDE Serial Monitor ([online reference](https://arduinogetstarted.com/tutorials/arduino-serial-monitor)) to write live timeseries data that can be copied and saved. Disable its *Show timestap* option beforehand.

In either case, set the *baud rate* to "9600 baud" to match the Arduino code and the *line ending* to "Both NL & CR" beforehand.

The Arduino serial plotter and monitor cannot be used simultaneously.
