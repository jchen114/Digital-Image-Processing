__author__ = 'Hooligan'
from PIL import Image
import numpy as np
import os.path
from scipy.misc import toimage
import math
from HW_4.ApplyFilter import ApplyFilter

IMG_FILE = 'Nintendo_Characters.jpg'


def gaussian_high_pass_image(img_file_name):
    img = Image.open(img_file_name).convert('L')
    str_grey_file = os.path.splitext(os.path.basename(img_file_name))[0] + '.png'
    img.save(str_grey_file)
    pix = np.asarray(img)
    img_width = pix.shape[1]
    img_height = pix.shape[0]
    hp_filter = create_centered_gaussian_high_pass(img_width * 2, img_height * 2, 10)
    ApplyFilter.apply_filter(pix, hp_filter, True)


def create_centered_gaussian_high_pass(width, height, std_dev):
    # Not going to center the filter
    g_filter = np.zeros((height, width))
    for r in range(0, height):
        for c in range(0, width):
            g_filter[r, c] = gaussian_value(r, c, width, height, std_dev)

    hpg_filter = 1 - g_filter
    return hpg_filter


def gaussian_value(row, col, width, height, std_dev):
    gauss_value = math.exp(-1 * math.pow(D(row, col, width, height),2) / (2 * math.pow(std_dev,2)))
    return gauss_value


def D(row, col, width, height):
    d_value = math.sqrt(math.pow(col - width/2, 2) + math.pow(row - height/2, 2))
    return d_value


if __name__ == "__main__":
    gaussian_high_pass_image(IMG_FILE)
    # Filter test
    #g_filter = create_centered_gaussian_high_pass(6, 6, 4)
    #print (g_filter)
    #lp_filter = create_noncentered_ideal_low_pass(15, 15, 3)
    #print(lp_filter)