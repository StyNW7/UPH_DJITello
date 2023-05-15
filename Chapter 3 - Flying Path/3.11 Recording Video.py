# import libraries

import time, cv2
from threading import Thread
from djitellopy import Tello

tello = Tello()
tello.connect()

# camera setup

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

# make a function or method

def videoRecorder():
 
# create a VideoWrite object, recording to ./video.avi

    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('Videos/video5.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

# we need to run the recorder in a separate thread, otherwise blocking options
# would prevent frames from getting added to the video

recorder = Thread(target=videoRecorder)
recorder.start()

# normal commands

tello.takeoff()

# these are the movement, you can change it whatever you want

tello.move_up(100)
tello.rotate_counter_clockwise(360)

# ends

tello.land()

keepRecording = False
recorder.join()
