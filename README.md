# SLU_Ground_Event
This repository holds the code for a satellite to ground interaction model. The model simulates a ground station recieving a command from the satellite, then commanding a camera to orient in a certain direction and begin tracking an object.
The structure of the program is:
1. Read the values from the magnetometer and actuate the stepper motors to rotate the camera to face a specified heading.
2. Begin looking for an object of a specified color
3. Track the object and actuate the pan/tilt servos in the corresponding directions to keep the object in frame. 
