#pip install opencv-contrib-python
#pip install cvzone

import cv2
cap = cv2.VideoCapture (0)
cam_w, cam_h = 640, 480
cap.set(3, cam_w)
cap.set(4, cam_h)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow("Camera Feed", img)
    cv2.waitKey(1)

