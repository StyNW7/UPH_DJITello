from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()
for i in range(4):
    tello.move_forward(30) # Move forward 30 cm
    tello.rotate_clockwise(90) # Rotate 90 degrees clockwise

tello.land()
