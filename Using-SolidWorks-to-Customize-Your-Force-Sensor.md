[Download as PDF](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/pdf/Using-SolidWorks-to-Customize-Your-Force-Sensor.pdf)

----

# Using SolidWorks to Customize Your Force Sensor

SolidWorks is a common CAD (computer-aided design) program with which Pithon sensors were developed. If you have SolidWorks 2019 or later, you can use it to customize them if necessary to meet the needs of your precise application.

Open [`mid_str_4T_sensing_and_elem.SLDPRT`](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/Development-Kit/Pithon%20Force%20Sensor,%20Accelerometer/mid_str_4T_sensing_and_elem.SLDPRT). This SolidWorks part file contains the base and cantilever beam of the force sensor as one component, and the conductive traces of the force sensor (including its sensing element and electrical terminals / contact pads) as another.

## Customize

**01. To adjust the distance from the back of the cantilever base to the start of the cantilever beam...**

 1. [In the left pane (the *FeatureManager Design Tree*), open the context menu for the Beam Surfaces *Extruded Boss/Base* feature.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/01/1.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Beam-Surfaces.png" style="zoom:50%;" /> \
    ​
    
 2. [Select *Edit Sketch*.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/01/2.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Edit-Sketch.png" style="zoom:50%;" /> \
    ​
    
 3. [Drag the leftmost line representing the back of the cantilever base, which will snap to the nearest half millimeter, or directly adjust its *X* position under *Additional Parameters* in the left pane to achieve finer resolution.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/01/3.png) We recommend *X* = 0 mm (lining it up with the origin of the coordinate system / $y$$z$-plane) for the sake of covering the primary set of conductive traces forming 4 terminals and one *sensing element*. Our default is *X* = --33 to also cover the secondary set. \
    ​
    
 4. Select *Exit Sketch*.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Exit-Sketch.png" style="zoom:50%;" /> \
    ​

Do this to vary the space for conductive traces or the mounting area. Do not design the exposed space for conductive traces to be a mounting area. The conductive traces are sensitive to material expansion/compression (as designed), including that applied by a mount.

Remember that this modification will change the bounding volume of the sensor.

**02. To adjust the length of the cantilever beam...**

 1. [In the left pane (the *FeatureManager Design Tree*), open the context menu for the Beam Surfaces *Extruded Boss/Base* feature.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/02/1.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Beam-Surfaces.png" style="zoom:50%;" /> \
    ​
    
 2. [Select *Edit Sketch*.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/02/2.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Edit-Sketch.png" style="zoom:50%;" /> \
    ​
    
 3. [Drag the rightmost line representing the free edge of the cantilever beam, which will snap to the nearest half millimeter, or directly adjust its *X* position under *Additional Parameters* in the left pane to achieve finer resolution.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/02/3.png) Our default is *X* = 45 mm. Alternately, adjust the *Length* parameter of either side edge of the cantilever beam. \
    ​
    
 4. Select *Exit Sketch*.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Exit-Sketch.png" style="zoom:50%;" /> \
    ​

Do this do vary the maximum deflection of the cantilever beam under a given load/force, particularly being applied to its free end, where the maximum deflection happens. Approximate the deflection of a beam without a notch using this formula:

$$ \small \sf \textsf{maximum deflection} = \dfrac{4 \left( \textsf{approximately vertical force} \right) \left( \textsf{beam length} \right)^3}{\left( \textsf{Young's modulus of the material} \right) \left( \textsf{beam width} \right) \left( \textsf{beam thickness} \right)^3} $$

Here, the *beam length* is really the distance from the start of the cantilever beam to wherever the force is applied along its length. The *Young’s modulus* is a mechanical property that is representative of elasticity and unique to the 3D printed material and its print settings. It has units of Newtons per square meter (N/m²) . Measure the maximum deflection and use the formula in reverse to approximate it. Only use the formula for small values of maximum deflection relative to the length of the cantilever beam.

The length *and* thickness of the cantilever beam greatly affect its maximum deflection. Making it twice as thick, for example, will have it deflect one eighth as much for the same force.

Remember that this modification will change the bounding volume of the sensor.

**03. To adjust the width of the cantilever beam...**

 1. [In the left pane (the *FeatureManager Design Tree*), open the context menu for the Beam Surfaces *Extruded Boss/Base* feature.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/03/1.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Beam-Surfaces.png" style="zoom:50%;" /> \
    ​
    
 2. [Select *Edit Sketch*.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/03/2.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Edit-Sketch.png" style="zoom:50%;" /> \
    ​
    
 3. [Drag the lines representing the sides of the cantilever beam, which will snap to the nearest half millimeter, or directly adjust their *Y* positions to ±(width)/2 under *Additional Parameters* in the left pane to achieve finer resolution.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/02/3.png) \
    ​
    
 4. Select *Exit Sketch*.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Exit-Sketch.png" style="zoom:50%;" /> \
    ​

Do this to vary the width of the force-sensitive area toward the free end.

**04. To adjust the thickness of the cantilever beam (and consequently shift the cantilever base by the same amount)...**

 1. [In the left pane, open the context menu for the Beam Surfaces *Extruded Boss/Base* feature.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/04/1.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Beam-Surfaces.png" style="zoom:50%;" /> \
    ​
    
 2. [Select *Edit Feature*.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/04/2.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Edit-Feature.png" style="zoom:50%;" /> \
    ​
    
 3. Drag the arrow showing the extrusion depth from the beam surfaces, which will snap to the nearest millimeter, or [directly adjust the *Depth* parameter in the left pane to achieve finer resolution](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/04/3.png). Our default is 2 mm. We often use 1 mm. \
    ​
    
 4. Select *OK*.

Do this to vary the maximum deflection of the cantilever beam under a given load/force, as in **02** above.

Remember that this modification will change the bounding volume of the sensor. Making the cantilever beam thicker, for example, will not take space from the cantilever base as you may expect.

**05. To change whether or not there is a hole at the free end of the cantilever beam...**

 1. [In the left pane, open the context menu for the Free End Hole *Extruded Cut* feature.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/05/1.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Free-End-Hole.png" style="zoom:50%;" /> \
    ​
    
 2. Select *Suppress* or *Unsuppress*. The Free End Hole Fillets, as a derived feature, will be automatically suppressed too, but should be manually unsuppressed along with the Free End Hole.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Suppress.png" style="zoom:50%;" /> or <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Unsuppress.png" style="zoom:50%;" /> \
    ​

Keep the free end hole if you are going to calibrate the force sensor by, for example, hanging known weights off the end of its cantilever beam, or if you are going to, say, tap a screw through it.

You likely do not need to change the position or diameter of the hole. If you do, you can follow similar instructions found in this section.

**06. To adjust the thickness of the cantilever base...**

 1. [In the left pane, open the context menu for the Cantilever Base *Extruded Boss/Base* feature.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/06/1.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Cantilever-Base.png" style="zoom:50%;" /> \
    ​
    
 2. [Select *Edit Feature*.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/06/2.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Edit-Feature.png" style="zoom:50%;" /> \
    ​
    
 3. Drag the arrow showing the extrusion depth from the bottom of the Beam Surfaces *Extruded Boss/Base* feature, which will snap to the nearest millimeter, or [directly adjust the *Depth* parameter in the left pane to achieve finer resolution](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/06/3.png). Our default is 4 mm beneath the cantilever beam, simply for a total thickness of 5 mm with the default 1-mm beam surfaces. \
    ​
    
 4. Select *OK*.

Remember that this modification will change the bounding volume of the sensor.

**07. To adjust the depth of the conductive traces...**

 1. [In the left pane, open the context menu for the Space for Conductive Traces *Extruded Cut* feature.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/07/1.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Space-for-Conductive-Traces.png" style="zoom:50%;" /> \
    ​
    
 2. [Select *Edit Feature*.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/06/2.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Edit-Feature.png" style="zoom:50%;" /> \
    ​
    
 3. [Adjust the *Depth* parameter in the left pane.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/07/3.png) Our default is 0.5 mm. \
    ​
    
 4. Select *OK*. \
    ​
    
 5. [In the left pane, open the context menu for the Conductive Traces *Extruded Boss/Base* feature](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/07/5.png), which uses the space made available by its matching *Extruded Cut* feature above.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Conductive-Traces.png" style="zoom:50%;" /> \
    ​
    
 6. Select *Edit Feature*.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Edit-Feature.png" style="zoom:50%;" /> \
    ​
    
 7. [Set the *Depth* parameter to be the same as in Step 3.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/07/7.png) \
    ​
    
 8. Select *OK*.

Do this to vary the resistance of the conductive traces, including the *sensing element*. Measure what will be the old resistance and approximate a new resistance using this formula:

$$ \small \sf \textsf{new resistance} = \textsf{old resistance} \ \! \cdot \dfrac{\: \, \textsf{old depth}}{\textsf{new depth}} $$

Only use the formula for wire-like conductive traces. Do not use It for electrical terminals / contact pads.

**08. To change whether or not there is a reference set of conductive traces...**

 1. [In the left pane, open the context menu for the mid_str_4T_Sensing_Elem Reference *Mirror* feature.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/08/1.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/mid_str_4T_sensing_elem-Reference.png" style="zoom:50%;" /> \
    ​
    
 2. Select *Suppress* or *Unsuppress*.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Suppress.png" style="zoom:50%;" /> or <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Unsuppress.png" style="zoom:50%;" /> \
    ​
    
 3. [Repeat steps 1–2 for the Space for mid_str_4T_Sensing_Elem Reference *Mirror* feature.](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/08/3.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Space-for-mid_str_4T_sensing_elem-Reference.png" style="zoom:50%;" /> \
    ​
    
 4. [Repeat steps 1–2 optionally for Mirror0](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/08/4.png), noted to be: \
    Space for lower jaws of crocodile clips for Electrical Contacts of mid_str_4T_Sensing_Elem Reference

**09. To change whether or not there are recesses/slots for crocodile clips...**

 1. [In the left pane, open the context menu for Cut-Extrude0](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/09/1.png), noted to be:
    Space for lower jaws of crocodile clips for Electrical Contacts of mid_str_4T_Sensing_Elem \
    ​
    
 2. Select *Suppress* or *Unsuppress*. Fillet0 and optionally Mirror0, as derived features, will be automatically suppressed too, but should be manually unsuppressed along with Cut-Extrude0.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Suppress.png" style="zoom:50%;" /> or <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Unsuppress.png" style="zoom:50%;" /> \
    ​

Keep the recesses/slots for crocodile clips if you are not yet going to use a conductive adhesive.

**10. To use your force sensor as an accelerometer...**

 1. [In the left pane, open the context menu for all of the Proof Mass and Mount features.](Using-SolidWorks-to-Customize-Your-Force-Sensor/10/1.png)
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Proof-Mass-and-Mount.png" style="zoom:50%;" /> \
    ​
    
 2. Select *Unsuppress*.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Unsuppress.png" style="zoom:50%;" /> \
    ​



The fillets are to better depict the 3D printing process for rendering purposes. You may opt to remove them entirely.

## Export

Before you can load the components of your 3D model into your 3D printing software, such as Ultimaker Cura, you need to export them from SolidWorks in more universal formats:

 1. To start, [change the left pane to show the *ConfigurationManager* tab.](Using-SolidWorks-to-Customize-Your-Force-Sensor/)
    
 2. Open our Export configuration.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Export.png" style="zoom:50%;" /> \
    ​
    
 3. Ensure that any and all of the above customizations are carried across.
    
 4. Ensure that all *Fillet* features have been suppressed.

### Export the Cantilever

 1. [Ensure that the Export Cantilever *Display State* is opened.](Using-SolidWorks-to-Customize-Your-Force-Sensor/)
    This hides everything except the light gray mid_str_4T_sensing *Body*, with its base and cantilever beam.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Export-Cantilever.png" style="zoom:50%;" /> \
    ​
    
 2. Select *File* > *Save **As**…*
    
     -  Name the export file “mid_str_4T_sensing” minus the file extension.
        
     -  Select *STL* (stereolithography mesh) for the file type.
        
        You can use other file types with similar purposes (e.g., STEP/STP) to your liking, given that they can also be imported into your 3D printing software.
    
 3. Confirm the generated triangular stereolithography mesh as previewed to save the export file.

### Export the Conductive Traces

 1. [Ensure that the Export Conductive Traces *Display State* is opened.](Using-SolidWorks-to-Customize-Your-Force-Sensor/)
    This hides everything except the black mid_str_4T_sensing_elem *Body*, with its *sensing element* and electrical terminals / contact pads. You can use this component for the reference set of conductive traces as well.
    
    <img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Using-SolidWorks-to-Customize-Your-Force-Sensor/Export-Conductive-Traces.png" style="zoom:50%;" /> \
    ​
    
 2. Select *File* > *Save **As***…
    
     -  Name the export file “mid_str_4T_sensing_elem” minus the file extension.
        
     -  Select *STL* (stereolithography mesh) for the file type.
        
        You can use other file types with similar purposes (e.g., STEP/STP) to your liking, given that they can also be imported into your 3D printing software.
    
 3. Confirm the generated triangular stereolithography mesh as previewed to save the export file.

----
