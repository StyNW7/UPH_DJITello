from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()

print(tello.get_battery())

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

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
    img = frame_read.frame
    cv2.imshow("drone", img)

    key = cv2.waitKey(1) & 0xff
    if key == 27: #ESC
        break
    elif key == ord("w"):         
        tello.move_forward(30)     
    elif key == ord('s'):         
        tello.move_back(30)     
    elif key == ord('a'):         
        tello.move_left(30)    
    elif key == ord('d'):         
        tello.move_right(30)     
    elif key == ord('e'):        
        tello.rotate_clockwise(90)     
    elif key == ord('q'):         
        tello.rotate_counter_clockwise(90)     
    elif key == ord('r'):         
        tello.move_up(30)     
    elif key == ord('f'):         
        tello.move_down(30)

    img = tello.get_frame_read().frame
    img, info = findFace(img)
    cv2.imshow("Face Tracking", img)
    
tello.land()
