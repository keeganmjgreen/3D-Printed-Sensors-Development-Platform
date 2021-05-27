# Product Manual Elements: [Arduino Language Reference](https://www.arduino.cc/reference/en/)

**Note:** Title case italics indicate the names of chapters, sections, pages, and headings (all unnumbered).

 -  Website navigation
 -  Language selection
 -  Left-hand column
    
     -  Small chapter-level table of contents (TOC)
     -  Links to other documentation
     -  [Licensing](https://creativecommons.org/licenses/)
     -  Contributions, e.g.,
        
         >  Find anything that can be improved? [Suggest corrections and new documentation via GitHub.](https://github.com/arduino/reference-en)
         >  
         >  Doubts on how to use Github? Learn everything you need to know in [this tutorial](https://create.arduino.cc/projecthub/Arduino_Genuino/contribute-to-the-arduino-reference-af7c37). 
    
 -  TOC page with inline header descriptions, e.g.,
    
     >  [*Language Reference*](https://www.arduino.cc/reference/en/) \
     >  Arduino programming language can be divided in three main parts: functions, values (variables and constants), and structure...
    
     >  [*Functions*](https://www.arduino.cc/reference/en/#functions) \
     >  For controlling the Arduino board and performing computations.
    
     >  [*Variables*](https://www.arduino.cc/reference/en/#variables) \
     >  Arduino data types and constants.
    
     >  [*Structure*](https://www.arduino.cc/reference/en/#structure) \
     >  The elements of Arduino (C++) code.
    
    Etc.
    
 -  *Functions*, e.g.,
    
    *Analog I/O*, e.g., *analogRead()* -- of particular relevance to us

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
        
        Language: [*analogReadResolution()*](https://www.arduino.cc/reference/en/language/functions/zero-due-mkr-family/analogreadresolution/)

        Example: [*Description of the analog input pins*](https://www.arduino.cc/en/Tutorial/Foundations/AnalogInputPins)
        
     -  Last page revision
     -  Last page build
     -  Link to "[edit this page](https://github.com/arduino/reference-en/edit/master/Language/Functions/Analog%20IO/analogRead.adoc)"
    
    *Communication*, e.g., *Serial* -- of particular relevance to us
    
 -  Footers, incl. copyright notice
