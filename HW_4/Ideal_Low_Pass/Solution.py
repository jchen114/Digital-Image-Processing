__author__ = 'Hooligan'
from PIL import Image
import numpy as np
import os.path
from HW_4.ApplyFilter import ApplyFilter
from scipy.misc import toimage

IMG_TO_BLUR = 'Nintendo_Characters.jpg'


def blur_image(img_file_name):
    img = Image.open(img_file_name).convert('L')
    str_grey_file = os.path.splitext(os.path.basename(img_file_name))[0] + '.png'
    img.save(str_grey_file)
    pix = np.asarray(img)
    img_width = pix.shape[1]
    img_height = pix.shape[0]
    lp_filter = create_noncentered_ideal_low_pass(img_width, img_height, 70)
    ApplyFilter.apply_filter(pix, lp_filter, False)
    # perform_shifted_multiplication(ft, img_height/3)
    # perform_nonshifted_multiplication(ft, img_height/3)


def create_noncentered_ideal_low_pass(width, height, cutoff):
    # Not going to center the filter
    lp_filter = np.zeros((height, width))
    for r in range(0, height):
        for c in range(0, cutoff - r):
            lp_filter[r, c] = 1
    return lp_filter


if __name__ == "__main__":
    blur_image(IMG_TO_BLUR)
    # Filter test
    #lp_filter = create_centered_ideal_low_pass(8, 8, 4)
    #print (lp_filter)
    #lp_filter = create_noncentered_ideal_low_pass(15, 15, 3)
    #print(lp_filter)