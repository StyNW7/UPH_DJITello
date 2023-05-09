import cv2

‘’’
this is a MUST library to use the camera.
you can learn more from this article:


https://www.topcoder.com/thrive/articles/what-is-the-opencv-library-and-why-do-we-need-to-know-about-it#:~:text=Capturing%20video%20using%20OpenCV,really%20useful%20for%20video%20analysis.
‘’’

tello.streamon()

# this command use to enable video stream

frame_read = tello.get_frame_read()

# this command to make a variable to get the frame that will show the picture capture by Tello’s camera

while True:

    img = frame_read.frame
    cv2.imshow("drone", img)

# these commands will show the image capture by Tello’s drone to our screen device

while True:

    img = frame_read.frame
    cv2.imwrite("drone", img)

# these commands will take a screenshot of the image captured by Tello’s drone and save it to the same folder as our code’s folder.
