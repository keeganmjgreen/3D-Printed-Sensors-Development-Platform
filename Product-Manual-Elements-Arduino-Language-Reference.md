# Product Manual Elements: [Arduino Language Reference](https://www.arduino.cc/reference/en/)

**Note:** Title case italics indicate the names of chapters, sections, and headings (all unnumbered).

 -  Table of contents with built-in header descriptions, e.g.,
    
    [*Language Reference*](https://www.arduino.cc/reference/en/) \
    Arduino programming language can be divided in three main parts: functions, values (variables and constants), and structure.
    
    [*Functions*](https://www.arduino.cc/reference/en/#functions) \
    For controlling the Arduino board and performing computations.
    
    [*Variables*](https://www.arduino.cc/reference/en/#variables) \
    Arduino data types and constants.
    
    [*Structure*](https://www.arduino.cc/reference/en/#structure) \
    The elements of Arduino (C++) code.
    
    Etc.
    
 -  *Functions*, e.g.,
    
    *Analog I/O*, e.g., *analogRead()*

     -  *Description*
         -  Inline with text: **table** with footnotes
     -  *Syntax*
        
     -  *Parameters*
        
     -  *Returns*
        
     -  *Example Code*
        
         -  Inline with text: **code block**, e.g.,
            
            ``` C++
            int analogPin = A3; // potentiometer wiper (middle terminal) connected to analog pin 3
                                // outside leads to ground and +5V
            int val = 0;  // variable to store the value read

            void setup() {
              Serial.begin(9600);           //  setup serial
            }

            void loop() {
              val = analogRead(analogPin);  // read the input pin
              Serial.println(val);          // debug value
            }
            ```
            
     -  *Notes and Warnings*
        
     -  *See Also*, e.g.,
        
        Language: *analogReadResolution()*

        Example: *Description of the analog input pins*
    
    *Communication*, e.g., *Serial*
