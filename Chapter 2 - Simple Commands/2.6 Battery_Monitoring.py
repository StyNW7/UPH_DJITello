from djitellopy import Tello # import library
tello = Tello() # define object
tello.connect() # make a connection

print(tello.get_battery()) # display the information of the battery status in the output section.
