from djitellopy import Tello
tello = Tello()
tello.connect()

tello.takeoff()

tello.move_forward(30) # Moves forward 30cm
tello.rotate_counter_clockwise(90) # rotate 90 degrees counterclockwise
tello.move_forward(50) # Moves forward 50cm
tello.rotate_counter_clockwise(90) # rotate 90 degrees counterclockwise
tello.move_forward(30) # Moves forward 30cm
tello.rotate_counter_clockwise(90) # rotate 90 degrees counterclockwise
tello.move_forward(50) # Moves forward 50cm
tello.rotate_counter_clockwise(90) # rotate 90 degrees counterclockwise

tello.land()
