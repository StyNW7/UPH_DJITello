import cv2
import numpy as np
from djitellopy import tello
import time

tello = tello.Tello()
tello.connect()

tello.takeoff()
tello.streamon()
tello.send_rc_control(0, 0, 25, 0)
time.sleep(0.5)

w, h = 800, 600
fbRange = [6200, 6800]
pid = [0.4, 0.4, 0]
pError = 0



def findFace(img):
    faceCascade = cv2.CascadeClassifier('folder name/haarcascade_frontalface_default.xml')
    imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imGray, 1.1, 4)

    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(img,'Face',(x+w,y+h), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.circle(img,(cx, cy), 5, (255, 0, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0,0], 0]
      
      

def trackFace(info, w, pid, pError):
    area = info[1]
    x, y = info[0]
    fb = 0

    error = x - w // 2
    speed = pid[0] * error + pid[1] * (error - pError)
    speed = int(np.clip(speed, -100, 100))

    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    elif area > fbRange[1]:
        fb = 10
    elif area < fbRange[0] and area != 0:
        fb = 50

    if x == 0:
        speed = 0
        error = 0
   
    print(speed, fb)

    tello.send_rc_control(0, fb, 0, speed)
    return error

  
  while True:
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    img, info = findFace(img)
    pError = trackFace(info, w, pid, pError)
    cv2.imshow("Face Tracking", img)
    if cv2.waitKey(1) == ord('q'):
        tello.land()
        break
