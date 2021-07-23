# Example Process Flow

This section further explores our Pithon platform for 3D printed sensors.

How do implementations of our Pithon platform get made? How will users produce 3D printed sensors for themselves? What does the process look like? To answer these questions, we will walk through an example process flow. \
​

We start with continuous fabrication, building our design from the ground up using conductive and structural plastics. \
​

First, we lay down electrically conductive traces on the 3D printing surface. These will make up the electrical terminals and sensing elements of our accelerometer and temperature sensor:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (1).png" alt="Figure (1)" style="zoom:100%;" /> \
​

We surround the conductive traces with what will become an enclosing structure of arbitrary size and shape:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (2).png" alt="Figure (2)" style="zoom:100%;" /> \
​

We cover the conductive traces as required with more of their enclosing structure:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (3).png" alt="Figure (3)" style="zoom:100%;" /> \
​

We have printed a cantilever beam for our accelerometer:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (4).png" alt="Figure (4)" style="zoom:100%;" /> \
​

Now, we keep going -- layer by layer -- leaving more space for a cavity:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (5).png" alt="Figure (5)" style="zoom:100%;" /> 

In practice, the cavity walls would slope both upward and inward to support subsequent layers, meaning that you wouldn't have to use a temporary support structure. \
​

We press-fit a steel ball into the space provided at the end of the accelerometer's cantilever beam:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (6).png" alt="Figure (6)" style="zoom:100%;" /> 

This will make it especially sensitive to acceleration. This weight a *proof mass*. Because it is metallic, the accelerometer can also be used as a magnetic field sensor. \
​

We cover the cavity with the rest of the arbitrarily-shaped enclosing structure:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (7).png" alt="Figure (7)" style="zoom:100%;" /> 

Note that especially by this point, the 3D printed part would be partially made up of a lattice -- this is the *infill pattern*. \
​

The 3D printing process of our part is soon complete. \
​

We remove the part from the surface of the 3D printer. It was printed upside-down. This served four purposes:

 1. Made it so that any problems with the conductive printing filament were detected early.
 2. Made the conductive plastic adhere to the surface of the 3D printer better.
 3. Improved the surface finish of our embedded sensors.
 4. Allowed our sensing elements to be as thin as 60 microns, such as for our temperature sensor. \
    ​

Our accelerometer and temperature sensor have been embedded into an arbitrary part. This design, for example, can be readily used for evaluation purposes as part of the Pithon platform:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (8).png" alt="Figure (8)" style="zoom:100%;" /> \
​

This is our embedded accelerometer:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (9).png" alt="Figure (9)" style="zoom:100%;" /> 

When the whole part speeds up or slows down, its cantilever beam bends up or down depending on the direction and amount of the acceleration it experiences. The material making up the top half of the beam gets compressed or stretched, especially at its base and on its surface. This is why we placed two strategically-sized notches in the base as shown. They 'concentrate' its mechanical stress toward its sensing element, which is at the beam surface. This makes it more sensitive to acceleration. \
​

This is our accelerometer's primary set of conductive traces:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (10).png" alt="Figure (10)" style="zoom:100%;" /> 

The zig-zag pattern in the middle is what forms its sensing element, a *strain gauge*, whose electrical resistance readily changes with mechanical strain. But the conductive traces' resistance also changes with temperature and humidity. \
​

This is where our accelerometer's secondary set of conductive traces comes into play:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (11).png" alt="Figure (11)" style="zoom:100%;" /> 

This is our accelerometer's secondary set of conductive traces. It can share an electrical terminal with the primary set and is its mirror image. But unlike the primary set, it isn't on a flexible beam. Because of this, it isn't sensitive to absent mechanical strain -- just temperature and humidity. These two "environmental conditions" are shared by both sets of conductive traces. Since the primary set responds to acceleration and environmental conditions similarly, and this secondary set responds only to the same environmental conditions, the acceleration by itself becomes known to us. \
​

This is our embedded temperature sensor:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (12).png" alt="Figure (12)" style="zoom:100%;" /> 

It measures the temperature of the surrounding air. Its sensing element is so small that it can point out of the arbitrarily-shaped structure too -- without getting in the way of anything. A kind of "guard rail" stops it from being damaged. Here, the sensing element is suspended midair in a cavity. Either case provides airflow. \
​

This is our temperature sensors' set of conductive traces:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (13).png" alt="Figure (13)" style="zoom:100%;" /> 

The sensing element's electrical resistance changes with temperature. A method called *four-terminal sensing* or *Kelvin sensing* is used to factor out temperature-dependent *contact resistances*. \
​

Now, we put liquid conductive paint (or conductive epoxy) on the large contact pads formed by the conductive traces:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (14).png" alt="Figure (14)" style="zoom:100%;" /> \
​

Before the conductive paint hardens, we bond wires to these contact pads:

<img src="https://raw.githubusercontent.com/keeganmjgreen/3D-Printed-Sensors-Manual-Demo/main/img/Example-Process-Flow/Figure (15).png" alt="Figure (15)" style="zoom:100%;" /> \
​

Finally, we connect our physical implementation of the Pithon platform to a microcontroller as shown and, optionally, a different power source, such as a coin cell embedded in the 3D printed part.

The microcontroller takes care of signal processing and digitally transmits the calibrated acceleration and temperature to where the data is needed. \
​
