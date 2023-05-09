from djitellopy import Tello
import cv2


tello = Tello()
tello.connect()


tello.streamon()
frame_read = tello.get_frame_read()


count = 0 #CHANGE DEPEND ON NUMBER OF SCREENSHOT IN THE PICTURES FOLDER #Count the number of screenshot


#tello.takeoff() 
#you can take off the drone or not


while True:
 
    img = frame_read.frame
    cv2.imshow("drone", img)


    key = cv2.waitKey(1) & 0xff


    if key == 27: # ESC
        break
    elif key == ord('p'):
        cv2.imwrite("screenshot " + str(count) + ".png", img)
        count += 1


tello.end()
#tello.land() 
#if you take off the drone, make sure to land it also
