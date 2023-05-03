from djitellopy import Tello
tello = Tello()
tello.connect()

tello.takeoff()

for i in range(2):
  tello.move_forward(30) #Moves forward 30cm
  tello.rotate_counter_clockwise(90) #rotate 90 degrees counterclockwise
  tello.move_forward(50) # Moves forward 30cm
  tello.rotate_counter_clockwise(90) # rotate 90 degrees counterclockwise

tello.land()
