# List of simple movement commands :
# tello.move_forward(x) # This command will move the drone forward x cm
# tello.move_back(x) # This command will move the drone backwards x cm
# tello.move_left(x) # This command will move the drone to the left x cm
# tello.move_right(x) # This command will move the drone to the right x cm
# tello.move_up(x) # This command will move the drone up x cm
# tello.move_down(x) # This command will move the drone down x cm

#  Simple movement example
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.takeoff() # Drone takes off
tello.move_forward(30) # Moves forward 30cm
tello.move_back(30) # Moves backward 30cm
tello.move_right(30) # Moves right 30cm
tello.move_left(30) # Moves left 30cm
tello.move_up(30) # Moves up 30cm
tello.move_down(30) # Moves down 30cm
tello.land() # Drone lands
