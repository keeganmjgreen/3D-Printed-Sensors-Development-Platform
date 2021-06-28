# Tips for Optionally Using *SolidWorks* to Build Upon Sensor Designs
    
 -  Use one SolidWorks part file (`.SLDPRT` filename extension) for the body of the sensor(s) and one for each sensing element (unless, of course, sensing elements are the same). For example:
    
    | Part of a Strain Sensor | Filename of SolidWorks Part      |
    |:------------------------|:---------------------------------|
    | Sensor body             | `mid_str_4T_sensing.SLDPRT`      |
    | Sensing element         | `mid_str_4T_sensing_elem.SLDPRT` |
    
 -  Under *Tools* > *Options* > *Document Properties* > *Units* > *Unit system*, select *MMGS (millimeter, gram, second)*. We used millimeters in our project development. Furthermore, 3D printer *slicing* software such as *Ultimaker Cura* uses grams.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Tips-for-Optionally-Using-SolidWorks-to-Build-Upon-Sensor-Designs-Figure-1.png" style="zoom:50%;" /> \
    ​
    
 -  Under *Tools* > *Options* > *Document Properties* > *Grid/Snap* > *Grid*, enable the *Display grid* and *Dash* options. Set the *Major grid spacing* to 1 mm, *Minor-lines per major* to 2, and *Snap points per minor* to 1.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Tips-for-Optionally-Using-SolidWorks-to-Build-Upon-Sensor-Designs-Figure-2.png" style="zoom:50%;" /> \
    ​
    
 -  Optionally, insert 'mask layouts' to trace in a SolidWorks sketch using *Tools* > *Sketch Tools* > [*Sketch Picture*](http://help.solidworks.com/2021/English/SolidWorks/sldworks/c_Sketch_Picture.htm).
    
     -  [Inserting Sketch Picture in Drawings --- SolidWorks Help](https://help.solidworks.com/2021/english/SolidWorks/sldworks/t_insert_sketch_picture_in_drawings.htm)
    
 -  As odd as it sounds, do not dimension or constrain sketches where snapping to the grid will suffice. This will make creating and modifying them easier and faster, and will keep them simpler and less 'busy'. There are many other ways to set and measure lengths. To delete all constraints in a sketch, whether they are automatically-created or not, select *Sketch* > *Display/Delete Relations* > *Relations* > *Delete All*.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Tips-for-Optionally-Using-SolidWorks-to-Build-Upon-Sensor-Designs-Figure-3.png" style="zoom:50%;" /> \
    ​
    
 -  Use linear sketch patterns.
    
 -  Properly name each SolidWorks sketch and feature (e.g., each extruded boss/base, extruded cut, fillet, chamfer, pattern, etc.). For example:
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Tips-for-Optionally-Using-SolidWorks-to-Build-Upon-Sensor-Designs-Figure-4.png" style="zoom:50%;" /> \
    ​

 -  Create parts right-side-up even if they are designed to be printed upside-down against the build plate.
    
 -  Create design features from the 'perspective' of a 3D printer.
