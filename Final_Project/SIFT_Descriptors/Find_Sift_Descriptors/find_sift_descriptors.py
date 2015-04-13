__author__ = 'jacobchen2272'
import cv2
import os
from Final_Project.SIFT_Descriptors.SIFT_DatabaseManager import DatabaseManager as dbm


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

    # Get the keypoints and descriptors
    (img1_color, img1_gray), kp1, des1 = find_sift_descriptors('Mario Images/Mario_1.jpg')
    (img2_color, img2_gray), kp2, des2 = find_sift_descriptors('Mario Images/Mario_2.jpg')
    (img3_color, img3_gray), kp3, des3 = find_sift_descriptors('Mario Images/Mario_3.jpg')

    # Store it into the database
    mongo_manager = dbm.DBManager()
    mongo_manager.insert_kp_des(kp1, des1)
    mongo_manager.insert_kp_des(kp2, des2)
    mongo_manager.insert_kp_des(kp3, des3)
