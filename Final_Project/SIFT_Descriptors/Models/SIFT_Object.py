__author__ = 'jacobchen2272'


class SIFT_Object:

    gray_image = None
    color_image = None
    keypoints = None
    descriptors = None

    def __init__(self, color, gray, kp, des):
        self.color_image = color
        self.gray_image = gray
        self.keypoints = kp
        self.descriptors = des