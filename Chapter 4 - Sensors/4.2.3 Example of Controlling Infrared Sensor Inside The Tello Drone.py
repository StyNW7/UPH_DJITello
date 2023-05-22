# Import necessary libraries 
from djitellopy import Tello
import time
import cv2

# Connect to Tello drone 
tello = Tello() 
tello.connect()

tello.takeoff()

height = tello.get_distance_tof()

print("Height: " + str(height))

# Check for obstacles

while True:

    if height <= 50: 
        tello.move_up(20) # Move up if obstacle detected 
        time.sleep(1) # Wait for the obstacle to pass 
    else: 
        tello.move_forward(100) # Move forward if no obstacle detected

    print("Height: " + str(height))

    # Maintain the same height

    if height >= 100: 
        tello.move_down(20) 
    elif height <= 80: 
        tello.move_up(20)

    print("Height: " + str(height))

    if cv2.waitKey(1) == 27: #ESC
        break

tello.land() 
tello.end()
