from picamera import PiCamera 
import time

camera = PiCamera()
# camera.capture('/home/ground/Desktop/Python/image.jpg')
# 
camera.start_preview()
# camera.start_recording('/home/ground/Desktop/Python/vid.h264')
time.sleep(3)
# camera.stop_recording()
camera.stop_preview()