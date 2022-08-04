from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
rawCap = PiRGBArray(camera)
time.sleep(.1)
camera.capture(rawCap, format = "bgr")
img = rawCap.array

cv2.imshow("Image",img)
cv2.waitKey(0)