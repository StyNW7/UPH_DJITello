from djitellopy import Tello
import time

tello = Tello() 
tello.connect() 
tello.takeoff()

v_up = 0
for i in range(4):
    tello.send_rc_control(32, 0, v_up, -59)
    time.sleep(9)
    tello.send_rc_control(0,0,0,0)
    time.sleep(1)
    tello.land()

tello.land()
