__author__ = 'jacobchen2272'
from Final_Project.SIFT_Descriptors.Models import K_Means as km
from Final_Project.SIFT_Descriptors.SIFT_Clustering import clustering as cl
from Final_Project.SIFT_Descriptors.Find_Sift_Descriptors import find_sift_descriptors as fsd
import numpy as np


# THRESHOLD
# See if the image is a picture of Mario by thresholding the distance from the image SIFT descriptors
# to the k-means cluster means. We find the distance from each descriptor to the cluster means and see which
# cluster the descriptor is closest to. We then add up all the distances. If the distance > THRESHOLD, then
# the image is not mario. Otherwise, we will say that it is mario.
def is_mario(img_file_name, k_obj, threshold):
    # Get the SIFT descriptors of the image
    sift_obj = fsd.find_sift_descriptors(img_file_name)
    descriptors = sift_obj.descriptors
    cluster_centers = k_obj.cluster_centers
    distance = calculate_distance(descriptors, cluster_centers)
    if distance > threshold:
        return True, distance
    else:
        return False, distance


def calculate_distance(descriptors, centers):
    distance = 0
    for descriptor in descriptors:
        # Find out which cluster the descriptor is closest to
        minimum_distance = -1
        for center in centers:
            dist = np.linalg.norm(descriptor - center)
            if minimum_distance == -1:
                minimum_distance = dist
            else:
                if dist < minimum_distance:
                    minimum_distance = dist
        distance += dist
    return distance


def is_true(obj):
    if obj == True:
        return 1
    else:
        return 0

if __name__ == "__main__":

    km_object = cl.cluster_sift_objects()

    sift_obj = fsd.find_sift_descriptors('Not Mario/Boo_1.jpg')
    print('is it mario? ' + str(is_mario('Not Mario/Boo_1.jpg', km_object, 100000)[0]))

    # Test distance calculation
    #sift_obj = fsd.find_sift_descriptors('Mario/Mario_1.jpeg')
    #print('Mario: ')
    #print('distance is ' + str(calculate_distance(sift_obj.descriptors, km_object.cluster_centers)))
    #sift_obj = fsd.find_sift_descriptors('Mario/Mario_2.jpg')
    #print('distance is ' + str(calculate_distance(sift_obj.descriptors, km_object.cluster_centers)))
    #sift_obj = fsd.find_sift_descriptors('Mario/Mario_3.jpg')
    #print('distance is ' + str(calculate_distance(sift_obj.descriptors, km_object.cluster_centers)))

    #print('Not Mario: ')
    #sift_obj = fsd.find_sift_descriptors('Not Mario/Boo_1.jpg')
    #print('Boo 1 distance is ' + str(calculate_distance(sift_obj.descriptors, km_object.cluster_centers)))
    #sift_obj = fsd.find_sift_descriptors('Not Mario/Boo_2.jpg')
    #print('Boo 2 distance is ' + str(calculate_distance(sift_obj.descriptors, km_object.cluster_centers)))
    #sift_obj = fsd.find_sift_descriptors('Not Mario/Boo_3.jpg')
    #print('Boo 3 distance is ' + str(calculate_distance(sift_obj.descriptors, km_object.cluster_centers)))
    #sift_obj = fsd.find_sift_descriptors('Not Mario/Boo_4.jpg')
    #print('Boo 4 distance is ' + str(calculate_distance(sift_obj.descriptors, km_object.cluster_centers)))
    #results = []
    #results.append(is_mario('Mario/Mario_1.jpeg', km_object))
    #results.append(is_mario('Mario/Mario_2.jpg', km_object))
    #results.append(is_mario('Mario/Mario_3.jpg', km_object))

    #reduce(lambda x, y: x + is_true(y), results, 0)