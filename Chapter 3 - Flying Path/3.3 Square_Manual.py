from djitellopy import Tello // import library

tello = Tello()
tello.connect()

tello.takeoff()
tello.move_forward(30) # Move forward 30 cm
tello.rotate_clockwise(90) # Rotate 90 degrees clockwise
tello.move_forward(30) # Move forward 30 cm
tello.rotate_clockwise(90) # Rotate 90 degrees clockwise
tello.move_forward(30) # Move forward 30 cm
tello.rotate_clockwise(90) # Rotate 90 degrees clockwise
tello.move_forward(30) # Move forward 30 cm
tello.rotate_clockwise(90) # Rotate 90 degrees clockwise

tello.land()
