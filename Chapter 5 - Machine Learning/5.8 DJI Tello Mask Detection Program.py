# FIRST PART (CONNECT TO WIFI)

# import libraries

import cv2
import torch
import numpy as np
from djitellopy import Tello
import time

# external packages

path = "C:/Users/User/Documents/All About Code/Python/UPH FK Ilmu Komputer/YOLOv5/best.pt"
model = torch.hub.load("ultralytics/yolov5", "custom", path, force_reload=True)

# method to detect mask

def mask_detect(frame):

    mask_count = 0
    results = model(frame)
    frame = np.squeeze(results.render())
    labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
    n = len(labels)
    x_shape, y_shape = frame.shape[1], frame.shape[0]
    for i in range(n):
        row = cord[i]
        if row[4] >= 0.30:
            x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(row[3] * y_shape)
            mask_count += 1
   
    return mask_count, frame


'''SECOND PART (CONNECT TO DJI TELLO DRONE)'''


# DJI Tello code

tello = Tello()
tello.connect()

print(tello.get_battery())
tello.streamon()

# shows frame

while True:


    frame = tello.get_frame_read().frame
    frame = cv2.resize(frame, (480, 360))
    mask_count, frame = mask_detect(frame)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(frame,"Mask Count: " + str(mask_count), (10, 50), font, 1, (255, 0, 0), 3)
    cv2.imshow("Mask Detection", frame)
    time.sleep(0.05)
    cv2.waitKey(1)
