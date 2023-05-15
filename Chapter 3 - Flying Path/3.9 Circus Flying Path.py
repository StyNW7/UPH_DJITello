# Import necessary libraries
from djitellopy import Tello
import time #library

# Connect to Tello drone
tello = Tello()
tello.connect()

tello.takeoff()

tello.flip_right() #flip command

tello.flip_forward() #flip command
time.sleep(2) #delay command

tello.flip_left() #flip command
time.sleep(0.5) #delay command

tello.flip_back() #flip command
time.sleep(1) #delay command

tello.land()
tello.end()
