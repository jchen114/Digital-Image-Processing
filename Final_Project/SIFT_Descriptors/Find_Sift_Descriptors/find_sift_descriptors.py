__author__ = 'jacobchen2272'
import cv2
import os
from Final_Project.SIFT_Descriptors.SIFT_DatabaseManager import DatabaseManager as dbm
from Final_Project.SIFT_Descriptors.Models import SIFT_Object as so
from matplotlib import pyplot as plt
import numpy as np
import math


def find_sift_descriptors(img_file_name):
    img = cv2.imread(img_file_name)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('Mario-bw.jpg', gray)
    sift = cv2.SIFT()
    (kp, des) = sift.detectAndCompute(gray, None)
    # If KP are describing background, get rid of them
    kp, des = drop_background(gray, kp, des)
    img_sift = cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    file_name = os.path.splitext('Mario SIFT Descriptors/' + os.path.basename(img_file_name))[0] + '-keypoints.jpg'
    cv2.imwrite(file_name,img_sift)
    sift_obj = so.SIFT_Object(img, gray, kp, des)
    return sift_obj


def drop_background(img, kps, des):
    index = []
    for x in range(0, len(kps)):
        kp = kps[x]
        coordinate = kp.pt
        if img[coordinate[1], coordinate[0]] >= 250:
            index.append(x)
    filtered_kps = np.delete(kps,index)
    filtered_des = np.delete(des, index, 0)
    return filtered_kps, filtered_des


def edge(img_file_name):
    img = cv2.imread(img_file_name, 0)
    edges = cv2.Canny(img,70,130)
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":

    #find_sift_descriptors('Mario Images/Mario_1_Filter.jpg')
    #find_sift_descriptors('Mario Images/Mario_2_Filter.jpg')
    #find_sift_descriptors('Mario Images/Mario_3_Filter.jpg')
    #find_sift_descriptors('Mario Images/Mario_4_Filter.jpg')
    #find_sift_descriptors('Mario Images/Mario_5_Filter.jpg')
    #find_sift_descriptors('Mario Images/Mario_6_Filter.jpg')
    #find_sift_descriptors('Mario Images/Mario_7_Filter.jpg')
    #find_sift_descriptors('Mario Images/Mario_8_Filter.jpg')

    #objects = []
    # Get the keypoints and descriptors
    #objects.append(find_sift_descriptors('Mario Images/Mario_1.jpg'))
    #objects.append(find_sift_descriptors('Mario Images/Mario_2.jpg'))
    #objects.append(find_sift_descriptors('Mario Images/Mario_3.jpg'))
    #objects.append(find_sift_descriptors('Mario Images/Mario_4.jpg'))
    #objects.append(find_sift_descriptors('Mario Images/Mario_5.jpg'))
    #objects.append(find_sift_descriptors('Mario Images/Mario_6.jpg'))
    #objects.append(find_sift_descriptors('Mario Images/Mario_7.jpg'))
    #objects.append(find_sift_descriptors('Mario Images/Mario_8.jpg'))

    find_sift_descriptors('Mario Images/Boo_4.jpg')

    # Store it into the database
    #mongo_manager = dbm.DBManager()
    #for sift_object in objects:
    #    mongo_manager.insert_kp_des(sift_object)
