# How To Test and Calibrate a Capacitive Humidity Sensor
Not everyone has access to their own environmental chambers to measure humidity. Luckily, a simple calibration can be performed with a simple wet salt test.

### Materials
- 1/2 cup of table salt
- 1/4 cup of water
- An open top container to hold the solution
- A resealable bag

This test takes no less than 8 hours so be sure to give yourself time to calibrate.

### Step 1
Prepare your capacitor so that it is able to be connected to the Pithon board. Take an initial measurement for a baseline value.

### Step 2
Pour 1/2 cup of table salt into the container previously gathered.

### Step 3
Pour the 1/4 cup of water into the cup on top of the salt. There shouldn't be any standing water at this point. Mix the water into the salt and pour any excess water out. The salt should have the appearance of a paste at this point.

### Step 4
Place the container with the solution into the resealable bag. Also place your sensor in the bag at this point, but leave the board outside of the bag. Notice: High humidity could potentially damage the Pithon board.

### Step 5
Seal the bag so that no air can enter or exit the bag. This can be assisted by taping down the entrance after the seal for added sealability. Leave the setup for at least 8 hours to give the environment a chance to reach its new relative humidity.

### Step 6
Measure the reading from the sensor once again. This new measurement should be at 75% RH where as the original was at around 40% RH (depending on your room's climate). Using these two points, the values can be cross-referenced with the calibration curve and create its own personal calibration curve to use.

At this point, the calibration settings can be input into the software to have your measurements return data with respect to the sensor.