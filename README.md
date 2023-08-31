# SLU_Ground_Event
This repository holds the code for a satellite to ground interaction model. The model simulates a ground station recieving a command from the satellite, then commanding a camera to orient in a certain direction and begin tracking an object.

Program Structure:
1. Read the values from the magnetometer and actuate the stepper motors to rotate the camera to face a specified heading.
2. Begin looking for an object of a specified color.
3. Track the object and actuate the pan/tilt servos in the corresponding directions to keep the object in frame. 



https://github.com/Nrxszv0/SLU_Ground_Event/assets/58677365/70348c0d-e89e-4651-9d60-0d0e6e227fd5

![SLU Ground Event Pic](https://github.com/Nrxszv0/SLU_Ground_Event/assets/58677365/74beb69c-8485-490a-a391-ed2ef17bb25e)
