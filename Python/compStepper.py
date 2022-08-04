# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
from math import atan2, degrees
import board
import adafruit_lis3mdl
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_lis3mdl.LIS3MDL(i2c)
kit = MotorKit(i2c=board.I2C())


calX = -29.06
calY = -8.48
calZ = 36.59

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    magnet_x -= calX
    magnet_y -= calY
    return vector_2_degrees(magnet_x, magnet_y)

intendedHeading = 30

while True:
    print("heading: {:.2f} degrees\tintended heading: {:.2f}".format(get_heading(sensor), intendedHeading))
    heading = get_heading(sensor)
    
    if heading < intendedHeading + 10 and heading > intendedHeading - 10:
        cwVal = 0
        ccwVal = 0
    elif heading < intendedHeading:
        cwVal = intendedHeading - heading
        ccwVal = 360 - intendedHeading + heading
    elif heading > intendedHeading:
        cwVal = 360 - heading + intendedHeading
        ccwVal = heading - intendedHeading    

    if cwVal != 0 and ccwVal !=0:
        if cwVal < ccwVal:
            print("CW")
            #rotate clockwise
            kit.stepper1.onestep(direction = stepper.BACKWARD)
        elif ccwVal < cwVal:
            #rotate counter clockwise
            print("CCW")
            kit.stepper1.onestep(direction = stepper.FORWARD)
        time.sleep(.025)



    time.sleep(0.2)