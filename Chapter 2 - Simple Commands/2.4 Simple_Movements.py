from djitellopy import Tello

tello = Tello()
tello.connect()

# Simple movement sequence
tello.move_forward(30) # Moves forward 30cm
tello.move_back(30) # Moves backward 30cm
tello.move_right(30) # Moves right 30cm
tello.move_left(30) # Moves left 30cm
tello.move_up(30) # Moves up 30cm
tello.move_down(30) # Moves down 30cm
