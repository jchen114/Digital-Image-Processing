__author__ = 'jacobchen2272'
import cv2
from Final_Project.SIFT_Descriptors.Find_Sift_Descriptors import Solution as fs
import scipy as sp
import numpy as np
from matplotlib import pyplot as plt


def match_descriptors_bf(img_file_1, img_file_2):
    (img1_color, img1_gray), kp1, des1 = fs.find_sift_descriptors(img_file_1)
    (img2_color, img2_gray), kp2, des2 = fs.find_sift_descriptors(img_file_2)
    # create BFMatcher object
    bf = cv2.BFMatcher()

    # Match descriptors.
    matches = bf.knnMatch(des1,des2, k=2)

    matches = [match[0] for match in matches]
    matches = sorted(matches, key=lambda val: val.distance)

    # Top 10 matches
    matches = matches[0:10]
    #cv2.imwrite('img_1.jpg', img1)
    #cv2.imwrite('img_2.jpg', img2)

    # view = visualize_matches(img1_gray, kp1, img2_gray, kp2, matches)
    view = draw_matches(img1_gray, kp1, img2_gray, kp2, matches)
    cv2.imwrite('view_bf.jpg', view)


def match_descriptors_flann(img_file_1, img_file_2):
    (img1_color, img1_gray), kp1, des1 = fs.find_sift_descriptors(img_file_1)
    (img2_color, img2_gray), kp2, des2 = fs.find_sift_descriptors(img_file_2)
    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params,search_params)

    matches = flann.knnMatch(des1,des2,k=2)
    matches = [match[0] for match in matches]
    # Sort the matches based on distance.  Least distance
    # is better
    matches = sorted(matches, key=lambda val: val.distance)

    # Top 10 matches
    matches = matches[0:10]

    view = draw_matches(img1_gray, kp1, img2_gray, kp2, matches)
    cv2.imwrite('view_flann.jpg', view)


def visualize_matches(img1, k1, img2, k2, sel_matches):
    # visualization
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    view = sp.zeros((max(h1, h2), w1 + w2, 3))
    view[:h1, :w1, 0] = img1
    view[:h2, w1:, 0] = img2
    view[:, :, 1] = view[:, :, 0]
    view[:, :, 2] = view[:, :, 0]

    for m in sel_matches:
        # draw the keypoints
        # print m.queryIdx, m.trainIdx, m.distance
        color = tuple([sp.random.randint(0, 255) for _ in xrange(3)])
        cv2.line(view, (int(k1[m.queryIdx].pt[0]), int(k1[m.queryIdx].pt[1])), (int(k2[m.trainIdx].pt[0] + w1), int(k2[m.trainIdx].pt[1])), color)

    return view


def draw_matches(img1, kp1, img2, kp2, matches):
    """
    My own implementation of cv2.drawMatches as OpenCV 2.4.9
    does not have this function available but it's supported in
    OpenCV 3.0.0

    This function takes in two images with their associated
    keypoints, as well as a list of DMatch data structure (matches)
    that contains which keypoints matched in which images.

    An image will be produced where a montage is shown with
    the first image followed by the second image beside it.

    Keypoints are delineated with circles, while lines are connected
    between matching keypoints.

    img1,img2 - Grayscale images
    kp1,kp2 - Detected list of keypoints through any of the OpenCV keypoint
              detection algorithms
    matches - A list of matches of corresponding keypoints through any
              OpenCV keypoint matching algorithm
    """

    # Create a new output image that concatenates the two images together
    # (a.k.a) a montage
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]

    out = np.zeros((max([rows1,rows2]),cols1 + cols2,3), dtype='uint8')

    # Place the first image to the left
    out[:rows1,:cols1,:] = np.dstack([img1, img1, img1])

    # Place the next image to the right of it
    out[:rows2,cols1:cols1+cols2,:] = np.dstack([img2, img2, img2])

    # For each pair of points we have between both images
    # draw circles, then connect a line between them
    for mat in matches:

        # Get the matching keypoints for each of the images
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        # x - columns
        # y - rows
        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt

        # Draw a small circle at both co-ordinates
        # radius 4
        # colour blue
        # thickness = 1
        cv2.circle(out, (int(x1),int(y1)), 4, (255, 0, 0), 1)
        cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)

        # Draw a line in between the two points
        # thickness = 1
        # colour blue
        cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (255, 0, 0), 1)
    return out


if __name__ == "__main__":
    match_descriptors_bf('Mario_1.jpg', 'Mario_2.jpg')
    #match_descriptors_flann('Mario_1.jpg', 'Mario-copy.jpg')