from djitellopy import Tello

tello = Tello()
tello.connect()

tello.takeoff() # Takeoff Command

tello.land() # Land Command
