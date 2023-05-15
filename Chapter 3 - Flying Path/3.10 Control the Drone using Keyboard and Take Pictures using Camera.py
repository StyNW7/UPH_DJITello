from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

count = 0 #Count the number of screenshot

tello.takeoff()

while True:

    img = frame_read.frame
    cv2.imshow("drone", img)

    key = cv2.waitKey(1) & 0xff

    if key == 27: # ESC
        break
    elif key == ord('p'):
        cv2.imwrite("Screenshot " + str(count) + ".png", img)
        count += 1

    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_back(30)
    elif key == ord('a'):
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == ord('l'):
        tello.rotate_clockwise(30)
    elif key == ord('j'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('u'):
        tello.move_up(30)
    elif key == ord('n'):
        tello.move_down(30)

tello.end()
tello.land()
