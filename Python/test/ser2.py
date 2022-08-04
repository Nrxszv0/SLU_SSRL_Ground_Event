import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.board)
GPIO.setup(7,50)
pwm = GPIO.PWM(7,50)
pwm.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(7,True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(7, False)
    