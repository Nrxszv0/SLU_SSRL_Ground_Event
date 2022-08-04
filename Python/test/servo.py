from gpiozero import Servo, Device
from gpiozero.pins.pigpio import PiGPIOFactory
import time

Device.pin_factory = PiGPIOFactory()
servo = Servo(4)
servo.value = 1
# while True:
    # servo.min()
    # time.sleep(0.5)
# while True:
#     servo.min()
#     time.sleep(.5)
#     servo.mid()
#     time.sleep(0.5)
#     servo.max()
#     time.sleep(0.5)
