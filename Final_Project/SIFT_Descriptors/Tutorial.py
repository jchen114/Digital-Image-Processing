__author__ = 'jacobchen2272'

import cv2
import numpy as np

IMG_FILE_NAME = "Mario.png"

if __name__ == "__main__":
    img = cv2.imread('Mario.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT()
    (kp, des) = sift.detectAndCompute(gray, None)
    img = cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite('sift_keypoints.jpg',img)