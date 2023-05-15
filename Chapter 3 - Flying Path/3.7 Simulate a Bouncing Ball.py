from djitellopy import Tello

tello = Tello()
tello.connect()

tello.takeoff()

heightUp = 60 #you can change the height to move drone up
heightDown = 35 #you can change the height to move the drone down

for i in range(3):
    tello.move_up(heightUp)
    tello.move_down(heightDown)

    heightUp -= 9 #the decrement the height of drone to moving up
    heightDown += 8 #the increment the height of drone to moving down

tello.move_up(heightUp)

tello.land()
