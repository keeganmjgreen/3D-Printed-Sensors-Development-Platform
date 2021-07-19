# Calibrating Your Force Sensor

## Materials and Preparation

 -  An untested force sensor with these defaults from `mid_str_4T_sensing_and_elem.SLDPRT`:
    ​
    
     -  A free end hole close to the end of the cantilever beam from which to suspend known weights. If you would like to use a force sensor that you have already printed without a free end hole, you can drill or punch a hole in the same place.
     -  A similarly thick cantilever base to avoid unwanted deflection, emulating being embedded into your comparably large parent 3D printed structure. If you do not need spaces for the lower jaws of crocodile clips in a thick cantilever base, and would prefer it to lessen your print time, you can glue a thinner cantilever base to a piece of wood to be used as the cantilever base.
     -  A reference set of conductive traces to correct for changes in temperature and humidity
     -  4-terminal sensing in each set of conductive traces
     -  Large electrical contact pads
     -  Spaces for lower jaws of crocodile clips (optional)
        ​
    
 -  An insulated double-ended crocodile clip jumper (or conductive paint/epoxy and lengths of thin wire stripped of its insulation on both ends) for *each* electrical contact
    
 -  A table clamp/vice
    
 -  Some string or more thin wire
    
 -  A laboratory weight set or similar

## Instructions

 1. Mount your clamp/vice on a table.
    
 2. Clamp onto your force sensor's cantilever base without the conductive traces being touched. Leave room for your crocodile clips if you are using them, room for the cantilever beam to bend downward, and room to suspend your weights from the free end of the cantilever beam.
    
 3. Tie your string or spare wire securely to the free end hole. Ensure that its mass is nearly 0 grams beforehand.
    
 4. Tie a loop at the other end of your string or spare wire.
    
 5. If you are not using weights with hooks, hang a lightweight clear plastic pouch from the loop to hold them. Ensure that its mass is nearly 0 grams beforehand.
    
 6. Clip one end of your crocodile clip jumpers into the terminal slots, onto the surfaces of the electrical terminals (or follow the instructions in **Preparing Electrical Contacts**).
    
 7. Now, assuming that you are using an Arduino microcontroller, open its IDE on your computer.
    
 8. Follow **2-Terminal Sensing for Real-Time Data Logging Using a Microcontroller** or **4-Terminal Sensing for Real-Time Data Logging Using a Microcontroller** as applicable per set of conductive traces. Use the Arduino Serial Monitor, and make these changes to the code under **Instructions – Programming**:
    
     1. Immediately after `Serial.begin(9600)`, append `Serial.setTimeout(100);`. This strikes a balance between a good sampling frequency (almost 10 per second) and stability over serial communication.
     2. Immediately before the end of the `loop()` function, append `Serial.print(Serial.readStringUntil("\r\n"));`. This will loop-back text that you enter in your serial monitor to log it for reasons that will become apparent.
    
 9. Plug in your Arduino using its USB cable.
    
10. Upload your modified code to the board using the Arduino IDE, after which it will begin running onboard.
    
11. In your Arduino IDE, open the serial monitor. You should see lines of electrical resistance values (in ohms) updated in real time from your sensor using your Arduino.
    
12. Wait momentarily while recording data -- say, roughly 100 samples. Be careful not to touch your sensor or its load.
    
13. Type "0 grams" into your serial monitor and *Send* this message to your Arduino and back (to record it conveniently in the same place) for the purpose of marking an upcoming change to the applied load. Example:
    
    ```
    ⁞
    3833.33
    0 grams
    3877.55
    ⁞
    ```
    
14. Gently suspend the smallest weight -- say, 4 grams -- from the cantilever beam's free end hole and wait briefly for your cantilever beam to settle under its new load.
    
15. Enter "4 grams" into your serial monitor. Example:
    
    ```
    ⁞
    3884.76
    4 grams
    3877.55
    ⁞
    ```
    
15. Repeat the last 4 steps for further incremental sums of masses.
    
16. Unplug your Arduino. Your serial monitor will 'freeze'.
    
17. Copy the partitioned runs of resistance data and save them into a text file, Excel workbook, etc.
    
18. Discard the resistance values between framed weight increments as being subject to the impulses of suddenly loading and unloading weights.
