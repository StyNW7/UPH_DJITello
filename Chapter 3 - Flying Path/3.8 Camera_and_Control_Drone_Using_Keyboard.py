from djitellopy import Tello # import library
import cv2, math, time # import library

tello = Tello() # define object
tello.connect() # connect

tello.streamon() # tello camera
frame_read = tello.get_frame_read() # make a variable that stores a frame from the tello's camera

tello.takeoff() #take off

while True: # looping
    img = frame_read.frame # make another variable
    cv2.imshow("drone", img) # show image

    key = cv2.waitKey(1) & 0xff # make a key variable
    if key == 27: #ESC
        break
    elif key == ord("w"):         
        tello.move_forward(30)     
    elif key == ord('s'):         
        tello.move_back(30)     
    elif key == ord('a'):         
        tello.move_left(30)    
    elif key == ord('d'):         
        tello.move_right(30)     
    elif key == ord('e'):        
        tello.rotate_clockwise(90)     
    elif key == ord('q'):         
        tello.rotate_counter_clockwise(90)     
    elif key == ord('r'):         
        tello.move_up(30)     
    elif key == ord('f'):         
        tello.move_down(30)
