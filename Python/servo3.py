from gpiozero import AngularServo,Device
from gpiozero.pins.pigpio import PiGPIOFactory
Device.pin_factory = PiGPIOFactory('127.0.0.1')
sp = AngularServo(22, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
st = AngularServo(25, min_angle =-75, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

while True:
    sp.angle = int(input("Enter Pan: "))
    st.angle = int(input("Enter Tilt: "))
    print(sp.angle)
    print(st.angle)
