# Tips for Optionally Using *SolidWorks* to Build Upon Sensor Designs

​
Use our sensor designs in SolidWorks at least as a starting point.
​

 -  Use one SolidWorks part file (`.SLDPRT` filename extension) for the body of the sensor(s) and one for each sensing element -- except, of course, for sensing elements that are the same. For example:
   
    | Part of a Strain Sensor | Filename of SolidWorks Part      |
    |:------------------------|:---------------------------------|
    | Sensor body             | `mid_str_4T_sensing.SLDPRT`      |
    | Sensing element         | `mid_str_4T_sensing_elem.SLDPRT` |
    
    Multibody parts or assemblies do not need to be created.
    ​
    
 -  Under *Tools* > *Options* > *Document Properties* > *Units* > *Unit system*, select *MMGS (millimeter, gram, second)*. We used millimeters in our project development. Furthermore, 3D printer *slicing* software such as *Ultimaker Cura* uses grams.
   
     -  [Units and Dimension Standard --- SolidWorks Help](http://help.solidworks.com/2021/English/SolidWorks/sldworks/HIDD_UNITS_DIM_STD.htm)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Tips-for-Optionally-Using-SolidWorks-to-Build-Upon-Sensor-Designs/Figure%20(1).png" style="zoom:50%;" />
    ​
    
 -  Under *Tools* > *Options* > *Document Properties* > *Grid/Snap* > *Grid*, enable the *Display grid* and *Dash* options. Set the *Major grid spacing* to 1 mm, *Minor-lines per major* to 2 if deemed necessary (1 otherwise), and *Snap points per minor* to 1. Creating and modifying SolidWorks sketches will be easier and faster.
   
     -  [Document Properties - Grid/Snap --- SolidWorks Help](https://help.solidworks.com/2021/English/SolidWorks/sldworks/HIDD_OPTIONS_GRID.htm)
     -  [Grid and Snap --- SolidWorks Help](http://help.solidworks.com/2021/English/SolidWorks/acadhelp/c_Grid_and_Snap.htm)
        ​
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Tips-for-Optionally-Using-SolidWorks-to-Build-Upon-Sensor-Designs/Figure%20(2).png" style="zoom:50%;" />
    ​
    
 -  Optionally, insert a 'mask layout' raster image to trace in a SolidWorks sketch using *Tools* > *Sketch Tools* > [*Sketch Picture*](http://help.solidworks.com/2021/English/SolidWorks/sldworks/c_Sketch_Picture.htm). Ensure that the pixel grid lines up with the sketch grid.
   
     -  [Inserting Sketch Picture in Drawings --- SolidWorks Help](https://help.solidworks.com/2021/english/SolidWorks/sldworks/t_insert_sketch_picture_in_drawings.htm)
        ​
    
 -  As odd as it sounds, do not dimension or constrain sketches where snapping to the grid will suffice. Creating and modifying them will be easier and faster, and they will be simpler and less 'busy'. There are many other ways to set and measure lengths. To delete all constraints in a sketch, whether they are automatically-created or not, select *Sketch* > *Display/Delete Relations* > *Relations* > *Delete All*.
    ​
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Tips-for-Optionally-Using-SolidWorks-to-Build-Upon-Sensor-Designs/Figure%20(3).png" style="zoom:50%;" />
    ​
    
 -  Use *linear sketch patterns*, as under *Sketch*.
    ​
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Tips-for-Optionally-Using-SolidWorks-to-Build-Upon-Sensor-Designs/Figure%20(4).png" style="zoom:50%;" />
    ​
     -  [Creating Linear Sketch Patterns --- SolidWorks Help](http://help.solidworks.com/2021/English/SolidWorks/sldworks/t_Creating_Linear_Sketch_Patterns.htm)
        ​
    
 -  Properly name each SolidWorks sketch and feature (e.g., each [extruded boss/base or extruded cut](https://help.solidworks.com/2021/english/solidworks/sldworks/t_creating_an_extrude_feature.htm), [fillet](https://help.solidworks.com/2021/english/SolidWorks/sldworks/t_create_fillets.htm), [chamfer](https://help.solidworks.com/2021/English/SolidWorks/sldworks/t_creating_chamfer_feature.htm), [pattern](http://help.solidworks.com/2021/English/SolidWorks/sldworks/c_Types_of_Patterns_Folder.htm), etc.). For example:
    ​
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Tips-for-Optionally-Using-SolidWorks-to-Build-Upon-Sensor-Designs/Figure%20(5).png" style="zoom:50%;" />
    ​

 -  Create parts right-side-up even if they are designed to be printed upside-down against the *build plate*. \
    ​
    
 -  Create design features from the 'perspective' of a 3D printer. For example: [Create SolidWorks sketches](http://help.solidworks.com/2021/English/SolidWorks/sldworks/c_Sketch.htm) on the *Top Plane* and extrude them away from it. Note that SolidWorks uses an engineering coordinate system in which the $y$-axis points up and the $z$-axis is normal to the vertical $xy$-plane. Whereas, 3D printing software such as *Ultimaker Cura* uses a more conventional coordinate system, in which the $z$-axis points up, normal to the *build plate*, whose surface is the horizontal $xy$-plane.
    ​

*Note:* SolidWorks is not forward compatible. Files cannot be opened or edited using a version of SolidWorks that is older than that with which they were originally created. The reverse works, albeit by converting them to the newer version.
​

## Resources

 -  [SolidWorks Help](https://help.solidworks.com/2021/English/SolidWorks/sldworks/r_welcome_sw_online_help.htm)
