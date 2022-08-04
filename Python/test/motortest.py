from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import board
import time
kit = MotorKit(i2c=board.I2C())
for i in range(200):    
    kit.stepper1.onestep(style=stepper.SINGLE)
    time.sleep(0.05)
for i in range(300):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    time.sleep(0.05)
for i in range(100):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
    time.sleep(0.05)
kit.stepper1.release()