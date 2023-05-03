from djitellopy import Tello

# Connect to Tello drone
tello = Tello() # Defines the Tello drone to tello
tello.connect() # Connects to the Tello drone

# Take off
tello.takeoff()

# Simple Flying Path
tello.move_forward(50) # Moves 50cm Forward
tello.rotate_clockwise(90) # Rotates 90° Clockwise
tello.move_forward(50) # Movies 50cm Forward
tello.rotate_clockwise(90) # Rotates 90° Clockwise


# Land Tello
tello.land()
