__author__ = 'jacobchen2272'
import cv2
import os
from Final_Project.SIFT_Descriptors.SIFT_DatabaseManager import DatabaseManager as dbm
from Final_Project.SIFT_Descriptors.Models import SIFT_Object as so


def find_sift_descriptors(img_file_name):
    img = cv2.imread(img_file_name)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('Mario-bw.jpg', gray)
    sift = cv2.SIFT()
    (kp, des) = sift.detectAndCompute(gray, None)
    img_sift = cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    file_name = os.path.splitext('Mario SIFT Descriptors/' + os.path.basename(img_file_name))[0] + '-keypoints.jpg'
    cv2.imwrite(file_name,img_sift)
    sift_obj = so.SIFT_Object(img, gray, kp, des)
    return sift_obj


if __name__ == "__main__":

    objects = []
    # Get the keypoints and descriptors
    objects.append(find_sift_descriptors('Mario Images/Mario_1.jpg'))
    objects.append(find_sift_descriptors('Mario Images/Mario_2.jpg'))
    objects.append(find_sift_descriptors('Mario Images/Mario_3.jpg'))
    objects.append(find_sift_descriptors('Mario Images/Mario_4.jpg'))
    objects.append(find_sift_descriptors('Mario Images/Mario_5.jpg'))
    objects.append(find_sift_descriptors('Mario Images/Mario_6.jpg'))
    objects.append(find_sift_descriptors('Mario Images/Mario_7.jpg'))
    objects.append(find_sift_descriptors('Mario Images/Mario_8.jpg'))


    # Store it into the database
    mongo_manager = dbm.DBManager()
    for sift_object in objects:
        mongo_manager.insert_kp_des(sift_object)
