[Download as PDF](https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Development-Platform/main/pdf/Example-Process-Flow.pdf)

----

<iframe width="420" height="315" src="https://www.youtube.com/embed/nedxR-Wya6k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> \
​

# Example Process Flow

This section further explores the Pithon platform for 3D printed sensors. \
​ \
How do implementations of the Pithon platform get made? How will you produce 3D printed sensors for yourself? What does the process look like? To answer these questions, we will walk through an example process flow. \
​

The process begins with continuous fabrication, building your design from the ground up using conductive and structural plastics. \
​

First, electrically conductive traces are deposited onto the 3D printing surface. These will make up the electrical terminals and sensing elements of your accelerometer and temperature sensor:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(1).png" alt="Deposit Conductive Plastic" style="zoom:50%;" /> \
​

The conductive traces are surrounded with with what will become your enclosing structure of arbitrary size and shape:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(2).png" alt="Surround with Structural Plastic" style="zoom:50%;" /> \
​

The conductive traces are covered as required with more of their enclosing structure:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(3).png" alt="Cover with Structural Plastic" style="zoom:50%;" /> \
​

A cantilever beam for your accelerometer has been printed:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(4).png" alt="Continue 3D Printing" style="zoom:50%;" /> \
​

Now, the 3D printing process continues -- layer by layer -- leaving more space for a cavity:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(5).png" alt="" style="zoom:50%;" />

By this point, the conductive 3D printing filament would have been swapped out for dissolvable filament for use as a temporary filler material to support upcoming layers. Alternatively, the cavity walls would slope both upward and *inward* to support subsequent layers, meaning that you wouldn't have to use a temporary support structure. \
​

You press-fit a steel ball into the space provided at the end of your accelerometer's cantilever beam:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(6).png" alt="Manually Insert Metal Ball" style="zoom:50%;" />

This will make it especially sensitive to acceleration. This weight is a *proof mass*. Because it is metallic, your accelerometer can also be used as a magnetic field sensor. \
​

The cavity is covered with the rest of your arbitrarily shaped enclosing structure:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(7).png" alt="Cover With Structural Plastic" style="zoom:50%;" />

Note that especially by this point, the 3D printed part would be partially made up of a lattice -- this is the *infill pattern*. \
​

The 3D printing process of our part is soon complete. \
​

You remove your part from the surface of your 3D printer. It was printed upside-down. This served four purposes:

 1. Made it so that any problems with the conductive printing filament were detected early.
 2. Made the conductive plastic adhere to the surface of your 3D printer better.
 3. Improved the surface finish of your embedded sensors.
 4. Allowed your sensing elements to be as thin as 60 microns, such as for your temperature sensor. \
    ​

A Pithon accelerometer and Pithon temperature sensor have been embedded into your arbitrary part. This design, for example, can be readily used for evaluation purposes as part of the Pithon platform:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(8).png" alt="" style="zoom:50%;" /> \
​

This is your embedded accelerometer:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(9).png" alt="Embedded Accelerometer" style="zoom:50%;" />

When the whole part speeds up or slows down, its cantilever beam bends up or down depending on the direction and amount of the acceleration it experiences. The material making up the top half of the beam gets compressed or stretched, especially at its base and on its surface. This is why two strategically sized notches are placed in the base as shown. They 'concentrate' its mechanical stress toward its sensing element, which is at the beam surface. This makes it more sensitive to acceleration.

The accelerometer may also be calibrated as a force sensor or magnetic field sensor under certain conditions (see end of section [**Pithon Accelerometer**](https://3d-printed-sensors-development-platform.readthedocs.io/en/latest/Pithon-Accelerometer.html)). \
​

This is your accelerometer's primary set of conductive traces:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(10).png" alt="Electrical Terminals and Strain-Sensitive Element" style="zoom:50%;" />

The zig-zag pattern in the middle is what forms its sensing element, a *strain gauge*, whose electrical resistance readily changes with mechanical strain. But the conductive traces' resistance also changes with temperature and humidity. \
​

This is where your accelerometer's secondary set of conductive traces comes into play:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(11).png" alt="Duplicate to Correct for Changes in Temperature and Humidity" style="zoom:50%;" />

The secondary set can share an electrical terminal with the primary set and is its mirror image. But unlike the primary set, it isn't on a flexible beam. Because of this, it isn't sensitive to absent mechanical strain -- just temperature and humidity. These two "environmental conditions" are shared by both sets of conductive traces. Since the primary set responds to acceleration and environmental conditions similarly, and this secondary set responds only to the same environmental conditions, the acceleration by itself becomes known. \
​

This is your embedded temperature sensor:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(12).png" alt="Embedded Temperature Sensor" style="zoom:50%;" />

It measures the temperature of the surrounding air. Its sensing element is so small that it can point out of your arbitrarily-shaped structure too -- without getting in the way of anything. A kind of "guard rail" stops it from being damaged. Here, the sensing element is suspended midair in a cavity. Either case provides airflow. \
​

This is your temperature sensors' set of conductive traces:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(13).png" alt="Electrical Terminals and Temperature-Sensitive Element" style="zoom:50%;" />

The sensing element's electrical resistance changes with temperature. A method called *four-terminal sensing* or *Kelvin sensing* is used to factor out temperature-dependent *contact resistances*. \
​

Now, you put liquid conductive paint (or conductive epoxy) on the large contact pads formed by the conductive traces:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(14).png" alt="Apply Conductive Paint to Main Electrical Terminals" style="zoom:50%;" /> \
​

Before the conductive paint hardens, you bond wires to these contact pads:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(15-2).png" alt="Add Wires to Main Electrical Terminals" style="zoom:50%;" /> \
​

Finally, you connect your physical implementation of the Pithon platform to your microcontroller as illustrated and, optionally, a different power source, such as a coin cell embedded in your 3D printed part.

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure%20(16).png" alt="Use With Your Microcontroller" style="zoom:50%;" /> \
Not shown: Minimal interface electronics.

The microcontroller takes care of signal processing and digitally transmits the calibrated acceleration and temperature to where the data is needed. \
​

## Using Filler Material

The following is a modified version of the Pithon implementation in the example process flow. It uses 3D printed filler material -- dissolvable PVA filament -- as a support structure (highlighted blue) for what becomes the base of the cavity.

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/platform_2%20with%20Filler%20Material.png" alt="" style="zoom:100%;" />

## Using Tapered Cavity Walls

The following is a modified version of the Pithon implementation in the example process flow. Its cavity has tapered walls to support subsequent layers, leaving potential for printing without a support structure. The top face of the enclosing structure is hidden is transparent to better show the cavity walls.

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/platform_2%20with%20Tapered%20Cavity%20Walls.png" alt="" style="zoom:100%;" />

----
