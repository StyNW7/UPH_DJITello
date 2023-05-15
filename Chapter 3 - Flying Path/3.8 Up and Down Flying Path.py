from djitellopy import Tello

tello = Tello()
tello.connect()

tello.takeoff()

for i in range(3):
    tello.move_forward(100)
    tello.land()
    tello.takeoff()

tello.move_up(70)

tello.land()
tello.end()
