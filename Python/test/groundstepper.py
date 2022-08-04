from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time
import board
kit = MotorKit(i2c=board.I2C())

# ^                                    ^
# |     Imports and initialization     |
#




# |     Put direction camera should face here |
# V     Value should be between -180 and 180  V
    intendedbearing = 







# |     Motor calibration              |
# V                                    V
while sensorbearing - 180 <= int(-1):
    kit.setpper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    time.sleep(0.05)
while sensorbearing - 180 >= 1:
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)





while q == 1

# | Interpreting sensor data (INCOMPLETE) |
# V                                       V
# This MUST be completed for the program to work.
# Pleast put sensor bearing calculations and data here
# use "sensorbearing" as the variable for the final bearing data
# make sure "sensorbearing" is an integer
# make sure it is run by the "while q == 1" function above



# |     Turning camera toward "event"  |
# V                                    V
    if sensorbearing - 180 <= intendedbearing - 1.25:
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.05)
    if sensorbearing - 180 >= intendedbearing + 1.25:
        kit.stepper.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(0.05)
    if sensorbearing - 180 >= intendedbearing - 1.25 and sensorbearing - 180 <= intendedbearing + 1.25:
        q = 2



time.sleep(60)
while sensorbearing - 180 <= int(-1):
    kit.setpper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    time.sleep(0.05)
    # Insert sensor data calculation here
while sensorbearing - 180 >= 1:
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    # Insert sensor data calculation here
kit.stepper1.release()