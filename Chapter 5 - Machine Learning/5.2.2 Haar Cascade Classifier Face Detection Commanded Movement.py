from djitellopy import Tello
import cv2
import numpy as np

#PARAMETERS
width = 200
height = 100
startCounter = 1

tellolet = Tello()
tellolet.connect()


print(tellolet.get_battery())

tellolet.streamoff()
tellolet.streamon()

def findFace(img):
    faceCascade = cv2.CascadeClassifier('tello drone/haarcascade_frontalface_default.xml')
    imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imGray, 1.1, 4)

    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img,(cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0,0], 0]
    

while True:
    frame_read = tellolet.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame, (width, height))

    if startCounter == 0:
        tellolet.takeoff()
        tellolet.move_forward(20)
        startCounter = 1


    img = tellolet.get_frame_read().frame
    img, info = findFace(img)
    cv2.imshow("Face Tracking", img)
    if cv2.waitKey(1) == ord('q'):
        tellolet.land()
        break
