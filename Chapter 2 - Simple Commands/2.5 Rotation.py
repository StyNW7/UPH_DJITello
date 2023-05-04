from djitellopy import Tello # import library
tello = Tello() # define object
tello.connect() # make a connection

tello.takeoff()

tello.rotate_counter_clockwise(90) #rotate the drone 90 degree in a counter clockwise direction
tello.rotate_clockwise(90) #rotate the drone 90 degree in a clockwise direction

tello.rotate_clockwise(360) #do full rotation in a clockwise direction
tello.rotate_counter_clockwise(360) #do full rotation in a counter clockwise direction

tello.rotate_clockwise(x) #rotate the drone x degree in a clockwise direction
tello.rotate_counter_clockwise(x) #rotate the drone x degree in a clockwise direction

tello.land()
