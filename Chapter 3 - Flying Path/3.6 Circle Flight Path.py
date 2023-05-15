from djitellopy import Tello
import time

tello = Tello()
tello.connect()
tello.takeoff()

tello.move_up(20)

tello.send_rc_control(0,0,0,0)
time.sleep(0.1)
# Turns motors on:
tello.send_rc_control(-100,-100,-100,100)
time.sleep(2)
tello.send_rc_control(0,10,20,0)
time.sleep(3)
tello.send_rc_control(0,0,0,0)
time.sleep(2)

v_up = 0
for i in range(4):
    tello.send_rc_control(40, -5, v_up, -35)
    time.sleep(4)
    tello.send_rc_control(0,0,0,0)
    time.sleep(0.5)
    tello.land()

tello.land()
