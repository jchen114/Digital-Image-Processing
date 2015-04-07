__author__ = 'Hooligan'
from PIL import Image
import numpy as np
import os.path
from HW_4.ApplyFilter import ApplyFilter
from HW_4.Gaussian_Low_Pass import Solution as glp
import math

IMG_NAME = 'Nintendo_Characters.jpg'


def log_image(img_file_name):
    img = Image.open(img_file_name).convert('L')
    str_grey_file = os.path.splitext(os.path.basename(img_file_name))[0] + '.png'
    img.save(str_grey_file)
    pix = np.asarray(img)
    img_width = pix.shape[1]
    img_height = pix.shape[0]
    lap_filter = create_centered_laplace_filter(img_width * 2, img_height * 2)
    glp_filter = glp.create_centered_gaussian_low_pass(img_width * 2, img_height * 2, 10)
    log_filter = lap_filter * glp_filter
    ApplyFilter.apply_filter(pix, log_filter, True)
    # perform_shifted_multiplication(ft, img_height/3)
    # perform_nonshifted_multiplication(ft, img_height/3)


def create_centered_laplace_filter(width, height):
    # Not going to center the filter
    lap_filter = np.zeros((height, width))
    for r in range(0, height):
        for c in range(0, width):
            lap_filter[r, c] = math.sqrt(math.pow(c - width / 2, 2) + math.pow(r - height / 2, 2))
    return lap_filter


if __name__ == "__main__":
    log_image(IMG_NAME)
    # Filter test
    #lap_filter = create_centered_laplace_filter(9, 9)
    #print (lap_filter)
    #lp_filter = create_noncentered_ideal_low_pass(15, 15, 3)
    #print(lp_filter)