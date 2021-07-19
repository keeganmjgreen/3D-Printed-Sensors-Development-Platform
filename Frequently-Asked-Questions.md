# Frequently Asked Questions #

1. **What 3D printer do you recommend using?**

    Monti 3D Printing Solutions has extensively used an [Ultimaker 3](https://www.printyourmind3d.ca/products/ultimaker-s3-studio-3d-printer?variant=30108183167042&currency=CAD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclid=CjwKCAjwos-HBhB3EiwAe4xM9yV7uknP2fZNOiuO5EQbyxLlzKxB9TC0XhfSdVipGeprtFxEK2JKfxoCgkwQAvD_BwE) for the development of the Pithon platform. As such, using an Ultimaker is highly recommended as it is inherintly compatible with all Pithon products. However, any upper-end consumer grade 3D printer should be capable of producing Pithon sensors. A [Prusa I3](https://shop.prusa3d.com/en/3d-printers/180-original-prusa-i3-mk3s-kit.html?gclid=Cj0KCQjwub-HBhCyARIsAPctr7y23jwYAAirW0L1mRWCBmT5142w8jbB9MeH0rOOPV-LDTmjdhxx6TgaAqLMEALw_wcB#), equivalent or any higher end model is recommended. Additionally, Monti recommends using a printer with dual extrusion capabilities as this will simplify the manufacturing process. The print resolution and consistency of lower grade printers cannot be garunteed.
    
2. **What 3D printing filament do you recommend using?**

    The majority of Monti's development has used [Proto-pasta Electrically Conductive Composite PLA](https://www.proto-pasta.com/products/conductive-pla) for conductive filament and [Ultimaker Silver Metallica PLA](https://www.voxelfactory.com/products/ultimaker-silver-metallic-pla-2-85mm-750g) as structural filament. Despite Monti's best efforts to make our manufacturing processes as cross-compatible as possible, other combinations of structural and conductive filament may not be compatible. Incompatible filaments may not adhere to eachother sufficiently and may seperate once cooled. We recommend using PLA based conductive filaments with PLA based structural filaments. Additionally, we recommend to use filaments from the same manufacturer as this will likely increase the chance they are compatible with eachother. Do not mix a PLA based filament with an ABS, or other material, filament as this increases the chance of incompatibility.

3. **Are conductive filaments difficult to print with?**

    Conductive filaments are typically quite brittle and require a higher heat to extrude. Using an Ultimaker 3, we have not experienced difficulties getting a consistent, high quality, extrusion of conductive filaments. Refer to the manufacturer's specifications for the conductive filaments, some require a minimum 3D printer nozzle diameter. Due to the brittleness of conductive filaments, particualr care must be taken to regularly clean your 3D printer's filament feeding mechanism and nozzle. Debris and conductive dust tend to be produced during the printing process and accumulates in the printer's feeder. Regularly clean the feeders as per the manufacturer's User Manual to prevent debris building up causing clogs. Additionally, if the 3D printer's feeder tension is too high, breaks or splits may develop in the filament which prevent the printer from feeding the material into the extruder.
    
4. **How Do I measure Capacitance?**

    After printing a capacitor, or capacitive sensor, it is recommended to verify the capacitor using a standard multimeter. Monti recommends using a multimeter accurate to within 0.1 pF. Start by measuring the resistance across the capacitor, the returned value should be either 'OL' for overload, or in the MΩ range. If you recieve smaller resistance values, the capacitor is likely shorted. In this case, you should attempt to reprint the sensor and/or improve print quality  by calibrating the printer, cleaning the print nozzle, cleaning the printer's feeding mechanism, or manually refeeding the conductive filament. Perform all these operations as per your 3D printer's User Manual. 
    
    After confirming that the capacitor is not shorted, measure the capacitance using a multimeter and confirm the value is close to the expected value as described in section XXX. Note that during sensor operation (while being measured by the microcontroller), the capacitance is never directly measured. It is indirectly measured using a process known as AC decoupling as described in section XXX. 
    
5. **What are typical resitance values of Pithon Sensors?**

    Resistors produced with conductive filament are dependent on the conductive filament used. Using [Proto-pasta Electrically Conductive Composite PLA](https://www.proto-pasta.com/products/conductive-pla), we typically produce resistors, or resistive sensors, with 3 to 15 kΩ resistance depending on the design. Conductive filaments with higher specified resistivity will produce resistors with a larger overall resistance.
    
6. **What are typical capacitance values of Pithon Sensors?**

    The capacitance values of Pithon capacitors depend on both the conductive filament and structural filament used. Using [Proto-pasta Electrically Conductive Composite PLA](https://www.proto-pasta.com/products/conductive-pla) and [Ultimaker Silver Metallica PLA](https://www.voxelfactory.com/products/ultimaker-silver-metallic-pla-2-85mm-750g), we produce 1 cm x 1 cm capacitors with an average capacitance of 12 pf. Doubling the area of the capacitor should lead to a four times increase in capacitance. 
