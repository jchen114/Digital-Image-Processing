__author__ = 'jacobchen2272'
import cv2
import os


def find_sift_descriptors(img_file_name):
    img = cv2.imread(img_file_name)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('Mario-bw.jpg', gray)
    sift = cv2.SIFT()
    (kp, des) = sift.detectAndCompute(gray, None)
    img_sift = cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    file_name = os.path.splitext('Mario SIFT Descriptors/' + os.path.basename(img_file_name))[0] + '-keypoints.jpg'
    cv2.imwrite(file_name,img_sift)
    return (img, gray), kp, des


if __name__ == "__main__":
    (img_color, img_gray), kp, des = find_sift_descriptors('Mario Images/Mario_1.jpg')
    (img_color, img_gray), kp, des = find_sift_descriptors('Mario Images/Mario_2.jpg')
    (img_color, img_gray), kp, des = find_sift_descriptors('Mario Images/Mario_3.jpg')

