# 2-Terminal Sensing for Real-Time Data Logging Using a Microcontroller

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/2-Terminal-Sensing-for-Real-Time-Data-Logging-Using-a-Microcontroller.png" style="zoom:50%;" />

$\uparrow$ Wiring diagram

## Materials and Preparation

 -  A microcontroller with at least 1 analog input pin, such as an Arduino [Uno](https://www.arduino.cc/en/Main/arduinoBoardUno&gt) or [Nano](https://www.arduino.cc/en/pmwiki.php?n=Main/ArduinoBoardNano)
 -  A 2-terminal sensor
 -  A 10-kΩ or similar through-hole resistor of known value

**For Testing**

 -  3 lengths of solid core hook-up wire stripped of its insulation on both ends
 -  3 insulated crocodile clip jumpers (double-ended)

**For Production** without a Circuit Board

 -  3 lengths of solid core hook-up wire stripped of its insulation on both ends
 -  Soldering setup
     -  Soldering iron with stand
     -  Lead-free solder
     -  Soldering sponge or similar
 -  3 lengths of thin heat shrink tubing
 -  2 lengths of thin (e.g., 30 AWG) wire stripped of its insulation on both ends.
 -  Conductive paint syringe
 -  Masking tape

## Instructions -- Assembly

**For Testing**

 1. Connect the hook-up wires to the `GND`, `A1`, and `5V` pins of the microcontroller.
    
 2. Connect the crocodile clip jumpers to the hook-up wires.
    
 3. Connect the resistor midway through the `A1` wire assembly.
    
 4. Connect the end of the `GND` wire assembly to the resistor.
    
 5. Connect the ends of the remaining wire assemblies, in order, to the `T1` and `T2` terminals of the 2-terminal sensor.

**For Production** without a Circuit Board

1. Connect the hook-up wires to the `GND`, `A1`, and `5V` pins of the microcontroller. Slip on the heat shrink tubing if necessary at this point.
   
3. Solder the thin wire to the latter 2 hook-up wires.
   
4. Solder the resistor midway through the `A1` wire assembly.
   
6. Solder the `GND` hook-up wire to the resistor.
   
   Apply the heat shrink tubing around all connections by evenly heating it using the soldering iron.
   
6. Connect the ends of the remaining wire assemblies, in order, to the `T1` and `T2` terminals of the 2-terminal sensor.
   
    1.  Coil the stripped ends of the thin wires into loops.
    2.  Carefully rest the loops on the center of the matching terminals' contact pads, holding the wires and sensor down using masking tape.
    3.  Carefully cover the wire loops with conductive paint within the borders of the contact pads.
    4.  Wait for the conductive paint to fully dry/harden.

## Instructions -- Programming

If you are using an [Arduino microcontroller](https://www.arduino.cc/en/Main/Products) (recommended), upload the following code to it using the [Arduino IDE](https://www.arduino.cc/en/Guide/Environment).

[`2_terminal_sensing_for_real_time_data_logging_using_a_microcontroller.ino`](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/2_Terminal_Sensing_for_Real_Time_Data_Logging_Using_a_Microcontroller.ino)

```c++
float R_series = 10e3;        // Known value of resistor in series with 2-terminal sensor.

void setup()
{
  Serial.begin(9600);         // Open communication with a computer via USB or with another device via UART.
}
void loop()
{
  float V_1 = analogRead(1);  // Measured voltage across series resistor.

  float I = V_1 / R_series;   // Calculated current through both series resistor and sensor.
  float V_sens = 5 - V_1;     // Calculated voltage across sensor.
  float R_sens = V_sens / I;  // Calculated resistance of sensor.

  Serial.print("R_sens:");
  Serial.print(R_sens);
  Serial.print("\t");

  Serial.print("lower:");
  Serial.print(0);
  Serial.print("\t");
 
  Serial.print("upper:");
  Serial.print(10e3);
  Serial.print("\n");
}
```
