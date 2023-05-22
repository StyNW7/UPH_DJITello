# Import necessary libraries 
from djitellopy import Tello
import time
import cv2

# Connect to Tello drone 
tello = Tello() 
tello.connect()

tello.takeoff()

# variables

height = 0
newHeight = 0
sameHeight = True

# while loop condition and comparasion between first height and new height after forward x cm

while sameHeight:

    height = tello.get_distance_tof()

    print("Height: " + str(height))
    time.sleep(0.5)

    tello.move_forward(100)

    time.sleep(2)

    newHeight = tello.get_distance_tof()

    print("New Height: " + str(newHeight))

    if newHeight == height:
        tello.move_forward(100)
    else:
        tello.move_up(50)
    
    if cv2.waitKey(1) == 27: #ESC
        break

tello.land()
tello.end()
