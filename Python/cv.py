import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lower_range = np.array([0, 50, 50])
    upper_range = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_range, upper_range)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        for contour in contours:
            if cv2.contourArea(contour) > 1000:
                # print(cv2.contourArea(contour))
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
                if coorX < width/2 - 50:
                    strX = "Left"
                elif coorX > width/2 + 50:
                    strX = "Right"
                else:
                    strX = "Center"

                if coorY < height/2 - 50:
                    strY = "Up"
                elif coorY > height/2 + 50:
                    strY = "Down"
                else:
                    strY = "Center"
                
                print(strX + "\t" + strY)
                #time.sleep(.2)

    
    # result = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow('mask', mask)
    # cv2.imshow('res', result)

    cv2.imshow('frame', frame)

    # cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()