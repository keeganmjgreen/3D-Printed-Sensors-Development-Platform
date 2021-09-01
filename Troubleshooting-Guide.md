[Download as PDF](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/pdf/Troubleshooting-Guide.pdf)

----

# Troubleshooting Guide #

**Conductive filament is not extruding.**

Conductive filament is typically quite brittle; the 3D printer's feeder can wear down the filament causing debris or dust to build up in the feeder. If not routinely cleaned, this debris can build up and cause the feeder to jam. Additionally, if the 3D printer's feeder has too high of a tension, it can cause the conductive filament to crack or split, preventing the feeder from functioning. Start by manually removing and the conductive filament. Observe the filament for obvious defects such as fractures. Using a pair of scissors, remove any visibly damaged region of filament. Reload the conductive filament into the 3D printer. If the problem persists, disassemble and clean your 3D printer's feeder mechanism. Finally, if the problem is still occurring, try reducing the tension of the feeder. Perform the above actions as per your 3D printer's User Manual.

**The sensor is not sticking to the print bed during printing.**

Separation from the print bed can occur if there is insufficient friction between the print bed and the print, or if there is any debris on the print bed. Start by thoroughly cleaning the print bed as per your printer's user manual. If the problem persists, try applying a layer of painter's tape to the print bed. Painter's tape will increase the friction between the print bed and the print, reducing risk of separation.

**I cannot remove the conductive filament from the printer.**

If care is not taken to routinely clean the printer's feeder when using conductive filament, debris can build up in the printer's feeder and nozzle. In extreme cases this can cause the filament to jam, making it very difficult to remove. If this occurs, follow your 3D printer's User Manual's Troubleshooting Guide. It should contain a section on how to manually remove jammed filament. After removing the filament, thoroughly clean the 3D printer's feeder and nozzle before reloading the material.

**The print quality of my sensor is poor.**

The most common cause of poor print quality when working with conductive filament is an insufficiently cleaned printer. Following your 3D printer's User Manual, try the following actions. Either complete the entire list, or complete each item separately and test printer performance after every step.

- Manually unload the conductive filament. Observe the conductive filament for obvious defects such as splits or fractures. Using a pair of scissors, remove all areas that have visible defects. Reload the conductive filament.
- Thoroughly clean the print bed.
- Disassemble the 3D printer's feeder. Using a compressed air canister, thoroughly clean any debris build up. Reassemble the feeder and reload the conductive filament.
- Manually unload the conductive filament. Load a generic PLA filament (non-conductive) and print a structure. Printing with an easier-to-print filament may dislodge any plastic stuck in the nozzle, resulting in higher quality prints.

**My capacitor has no measurable capacitance.**

The most likely issue is that the capacitor is shorted. Using a standard multimeter, measure the resistance across the capacitor. The measured resistance should be 'OL' for overload or in the megaohm (MΩ) range. If the resistance is lower, the capacitor is shorted. Try improving the print quality of your 3D printer by following the suggestion provided above in Troubleshooting Guide: 'The print quality of my sensor is poor'. Attempt to print the capacitor again. A properly functioning 3D printer should not produce shorted capacitors.

----
