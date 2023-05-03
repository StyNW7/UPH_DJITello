from djitellopy import Tello
tello = Tello()
tello.connect()

tello.takeoff() # Takes off
tello.rotate_clockwise(90) # Rotates 90° clockwise
tello.move_forward(50) # Moves 50cm forward
tello.rotate_counter_clockwise(135) # Rotates 135° counter clockwise
tello.move_forward(50) # Moves 50cm forward
tello.rotate_clockwise(135) # Rotates 135° clockwise
tello.move_forward(50) # Moves 50cm forward
tello.land() # Lands
