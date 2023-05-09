# Import necessary libraries
from djitellopy import Tello
import time

# Connect to Tello drone
tello = Tello()
tello.connect()

tello.takeoff()

height = tello.get_distance_tof()

print(height)

# Check for obstacles

if height <= 50:
    tello.move_up(20) # Move up if obstacle detected
    time.sleep(1) # Wait for the obstacle to pass
else:
    tello.move_forward(20) # Move forward if no obstacle detected

# Maintain the same height

if height >= 100:
    tello.move_down(20)
elif height <= 80:
    tello.move_up(20)

print(height)

tello.land()
tello.end()
