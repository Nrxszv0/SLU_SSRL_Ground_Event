import numpy as np
import cv2
import time
from gpiozero import AngularServo,Device
from gpiozero.pins.pigpio import PiGPIOFactory
from math import atan2, degrees
import board
import adafruit_lis3mdl
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
Device.pin_factory = PiGPIOFactory('127.0.0.1')
sp = AngularServo(22, min_angle =-90, max_angle=90,min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
st = AngularServo(25, min_angle =-10, max_angle=90, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
sp.angle = 0
st.angle = 20
cap = cv2.VideoCapture(0)

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

findDirection = True
while findDirection:
    print("heading: {:.2f} degrees\tintended heading: {:.2f}".format(get_heading(sensor), intendedHeading))
    heading = get_heading(sensor)
    
    if heading < intendedHeading + 10 and heading > intendedHeading - 10:
        cwVal = 0
        ccwVal = 0
        findDirection = False
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

while(True):
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lower_range = np.array([40, 50, 50])
    upper_range = np.array([75, 255, 255])

    mask = cv2.inRange(hsv, lower_range, upper_range)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # time.sleep(0.2)

    if len(contours) >0:
        for contour in contours:
            if cv2.contourArea(contour) > 2000:
                print(cv2.contourArea(contour))
                # print(str(width) + "\t" + str(height))
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3)
                coorX =  int((x+x+w)/2) 
                coorY = int((y+y+h)/2)
                cirCenter = coorX, coorY
                # print(cirCenter)
                BLUE = (255, 0, 0)
                axes = 0, 0
                angle = 0
                cv2.ellipse(frame, cirCenter, axes, angle, 0, 360, BLUE, 20)
                
                strX =""
                strY = ""
                serP = 0
                serT = 0
                if coorX < width/2 - 100:
                    strX = "Left"
                    serP = 1
                    
                elif coorX > width/2 + 100:
                    strX = "Right"
                    serP = -1
                else:
                    strX = "Center"
                    serP = 0

                if coorY < height/2 - 100:
                    strY = "Up"
                    serT = 1
                elif coorY > height/2 + 100:
                    strY = "Down"
                    serT = -1
                else:
                    strY = "Center"
                    serT = 0
                if sp.angle > -88 and sp.angle < 88:
                    sp.angle += serP
                if st.angle > -10 and st.angle < 88:
                    st.angle += serT
                    print(st.angle)
                
                print(strX + "\t" + strY)
                time.sleep(.125)

    
    # result = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow('mask', mask)
    # cv2.imshow('res', result)

    cv2.imshow('frame', frame)

    # cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()