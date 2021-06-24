# Four-Terminal Sensing for Real-Time Data Logging Using a Microcontroller

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Four-Terminal-Sensing-for-Real-Time-Data-Logging-Using-a-Microcontroller.png" style="zoom:50%;" />

Wiring diagram $\uparrow$

## Materials and Preparation

 -  A microcontroller with at least three analog input pins, such as an Arduino [Uno](https://www.arduino.cc/en/Main/arduinoBoardUno&gt) or [Nano](https://www.arduino.cc/en/pmwiki.php?n=Main/ArduinoBoardNano)
 -  A four-terminal sensor
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
 -  5 lengths of thin heat shrink tubing
 -  4 lengths of thin (e.g., 30 AWG) wire stripped of its insulation on both ends.
 -  Conductive paint syringe
 -  Masking tape

## Instructions -- Assembly

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Four-Terminal-Sensor-Pinout.png" style="zoom:50%;" />

Pinout of a four-terminal sensor $\uparrow$

**For Testing**

 1. Connect the hook-up wires to the `GND`, `A1`, `A2`, `A3`, and `5V` pins of the microcontroller.
    
 2. Connect the crocodile clip jumpers to the hook-up wires.
    
 3. Connect the resistor midway through the `A1` wire assembly.
    
 4. Connect the end of the `GND` wire assembly to the resistor.
    
 5. Connect the ends of the remaining wire assemblies, in order, to the `T1`, `T2`, `T3`, and `T4` terminals of the four-terminal sensor.

**For Production** without a Circuit Board

1. Connect the hook-up wires to the `GND`, `A1`, `A2`, `A3`, and `5V` pins of the microcontroller. Slip on the heat shrink tubing if necessary at this point.
   
3. Solder the thin wire to the latter four hook-up wires.
   
4. Solder the resistor midway through the `A1` wire assembly.
   
6. Solder the `GND` hook-up wire to the resistor.
   
   Apply the heat shrink tubing around all connections by evenly heating it using the soldering iron.
   
6. Connect the ends of the remaining wire assemblies, in order, to the `T1`, `T2`, `T3`, and `T4` terminals of the four-terminal sensor.
   
    1.  Coil the stripped ends of the thin wires into loops.
    2.  Carefully rest the loops on the center of the matching terminals' contact pads, holding the wires and sensor down using masking tape.
    3.  Carefully cover the wire loops with conductive paint within the borders of the contact pads.
    4.  Wait for the conductive paint to fully dry/harden.

## Instructions -- Programming

If you are using an Arduino microcontroller, download the following code to it.

```c++
float R_series = 10e3;

void setup()
{
  Serial.begin(9600);
}
void loop()
{
  float V_1 = analogRead(1);
  float V_2 = analogRead(2);
  float V_3 = analogRead(3);

  float I = V_1 / R_series;
  float V_elem = V_3 - V_2;
  float R_elem = V_elem / I;

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
