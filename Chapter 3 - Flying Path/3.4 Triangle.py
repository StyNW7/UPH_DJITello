from djitellopy import Tello
tello = Tello()
tello.connect()

tello.takeoff()

tello.rotate_clockwise(45) # Rotates 45° clockwise
tello.move_forward(50) # Moves 50cm forward
tello.rotate_clockwise(90) # Rotates 90° clockwise
tello.move_forward(50) # Moves 50cm forward
tello.rotate_clockwise(135) # Rotates 135° clockwise
tello.move_forward(71) # Moves 50cm forward
tello.rotate_clockwise(90) # Rotates 90° clockwise

tello.land()
