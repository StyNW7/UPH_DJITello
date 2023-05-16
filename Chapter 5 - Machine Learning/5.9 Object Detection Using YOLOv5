# CONNECT TO WIFI FIRST!

# import libraries

import cv2
import torch
import numpy as np
from djitellopy import Tello
import time

# YOLOv5 Packages

model = torch.hub.load("ultralytics/yolov5","yolov5x")

# method to detect mask

def object_detect(frame):


    object_count = 0
    results = model(frame)
    frame = np.squeeze(results.render())
    labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
    n = len(labels)
    x_shape, y_shape = frame.shape[1], frame.shape[0]
    for i in range(n):
        row = cord[i]
        if row[4] >= 0.30:
            x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(row[3] * y_shape)
            object_count += 1
   
    return object_count, frame


# CONNECT TO THE DJI TELLO DRONE’S WIFI!


# DJI Tello code

tello = Tello()
tello.connect()

print(tello.get_battery())
tello.streamon()

# shows frame

while True:

    frame = tello.get_frame_read().frame
   
    object_count, frame = object_detect(frame)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(frame,"Object Count: " + str(object_count), (10, 50), font, 1, (255, 0, 0), 3)
    cv2.imshow("Object Detection", frame)
    time.sleep(0.05)
    cv2.waitKey(1)
