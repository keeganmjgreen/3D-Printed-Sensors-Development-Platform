# 4-Terminal Sensing for Real-Time Data Logging Using a Microcontroller

4-terminal sensing is slightly more complicated to set up than 2-terminal sensing and less compact in implementation. However, it is more consistent between sensors and more repeatable for a given sensor. It virtually eliminates the effect of contact resistance and other *parasitic* resistances on the measurement of a resistive sensing element.

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/4-Terminal-Sensing-for-Real-Time-Data-Logging-Using-a-Microcontroller.png" style="zoom:50%;" />

$\uparrow$ Wiring diagram. Pins `A0` -- `A3` are analog input pins to the microcontroller.

## Materials and Preparation

 -  A microcontroller with at least 3 analog input pins, such as an Arduino [Uno](https://www.arduino.cc/en/Main/arduinoBoardUno&gt) or [Nano](https://www.arduino.cc/en/pmwiki.php?n=Main/ArduinoBoardNano)
 -  A 4-terminal sensor
 -  A 10-kΩ or similar through-hole resistor of known value

**For Testing**

 -  5 lengths of solid core hook-up wire stripped of its insulation on both ends
 -  5 insulated crocodile clip jumpers (double-ended)

**For Production** without a Circuit Board

 -  5 lengths of solid core hook-up wire stripped of its insulation on both ends
 -  Soldering setup
     -  Soldering iron with stand
     -  Lead-free solder
     -  Soldering sponge or similar
 -  5 pieces of thin heat shrink tubing
 -  4 lengths of thin (e.g., 30 AWG) wire stripped of its insulation on both ends.
 -  Conductive paint syringe
 -  Masking tape

## Instructions -- Assembly

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/4-Terminal-Sensor-Pinout.png" style="zoom:50%;" />

$\uparrow$ Pinout of a 4-terminal sensor.

**For Testing**

 1. Connect the hook-up wires to the `GND`, `A1`, `A2`, `A3`, and `5V` pins of the microcontroller.
    
 2. Connect the crocodile clip jumpers to the hook-up wires.
    
 3. Connect the resistor midway through the `A1` wire assembly.
    
 4. Connect the end of the `GND` wire assembly to the resistor.
    
 5. Connect the ends of the remaining wire assemblies, in order, to terminals `T1` -- `T4` of the 4-terminal sensor.

**For Production** without a Circuit Board

 1. Connect the hook-up wires to the `GND`, `A1`, `A2`, `A3`, and `5V` pins of the microcontroller. \
    Slip on the heat shrink tubing if necessary at this point.
    
 2. Solder the thin wire to the latter 4 hook-up wires.
    
 3. Solder the resistor midway through the `A1` wire assembly.
    
 4. Solder the `GND` hook-up wire to the resistor.
    
    Apply the heat shrink tubing around all connections by evenly heating it using the soldering iron.
    
 5. Connect the ends of the remaining wire assemblies, in order, to terminals `T1` -- `T4` of the 4-terminal sensor.
    
     1. Coil the stripped ends of the thin wires into loops.
     2. Carefully rest the loops on the center of the matching terminals' contact pads, holding the wires and sensor down using masking tape.
     3. Carefully cover the wire loops with conductive paint within the borders of the contact pads.
     4. Wait for the conductive paint to fully dry/harden.

## Instructions -- Programming

If you are using an [Arduino microcontroller](https://www.arduino.cc/en/Main/Products) (recommended), upload the following code to it using the [Arduino IDE](https://www.arduino.cc/en/Guide/Environment).

[`4_Terminal_Sensing_for_Real_Time_Data_Logging_Using_a_Microcontroller.ino`](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/4_Terminal_Sensing_for_Real_Time_Data_Logging_Using_a_Microcontroller.ino)

```c++
float R_series = 10e3;  // Known value of resistor in series with 4-terminal sensor.

float V_1;
float V_2;
float V_3;

float I;
float V_elem;
float R_elem;

void setup()
{
    Serial.begin(9600);   // Open communication with a computer via USB or with another device via UART.
}
void loop()
{
    V_1 = analogRead(1);  // Measured voltage across series resistor.
    V_2 = analogRead(2);  // Measured voltage looking into the 4-terminal sensor at terminal `T2`.
    V_3 = analogRead(3);  // Measured voltage looking into the 4-terminal sensor at terminal `T3`.
    
    I = V_1 / R_series;   // Calculated current through both series resistor and 4-terminal sensor.
    V_elem = V_3 - V_2;   // Calculated voltage across sensing element.
    R_elem = V_elem / I;  // Calculated resistance of sensing element.
    
    Serial.print("R_elem:");
    Serial.print(R_elem);
    Serial.print("\t");
    
    Serial.print("lower:");
    Serial.print(0);
    Serial.print("\t");
    
    Serial.print("upper:");
    Serial.print(10e3);
    Serial.print("\n");
}
```

### Additional Resources

[Arduino Language Reference](https://www.arduino.cc/reference/)

 -  Communication -- [Serial](https://www.arduino.cc/reference/en/language/functions/communication/serial/)
 -  Analog input/output -- [analogRead()](https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/)
