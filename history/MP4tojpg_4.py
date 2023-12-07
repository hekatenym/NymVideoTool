from cv2 import cv2
import os
vc = cv2.VideoCapture('')
rval = vc.isOpened()
n=0
m=0
while rval:
    rval, frame = vc.read()
    if n % 4 == 0:
        cv2.imwrite(''+ str(m) + '.jpg', frame)
        print(''+ str(m) + '.jpg')
        m = m + 1
    n = n + 1
vc.release()