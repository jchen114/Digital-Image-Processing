__author__ = 'Hooligan'
from PIL import Image
import numpy as np
import os.path
from scipy.misc import toimage
from HW_4.ApplyFilter import ApplyFilter

IMG_FILE = 'Nintendo_Characters.jpg'


def high_pass_image(img_file_name):
    img = Image.open(img_file_name).convert('L')
    str_grey_file = os.path.splitext(os.path.basename(img_file_name))[0] + '.png'
    img.save(str_grey_file)
    pix = np.asarray(img)
    img_width = pix.shape[1]
    img_height = pix.shape[0]
    ideal_hp_filter = create_noncentered_ideal_high_pass(img_width, img_height, 70)
    ApplyFilter.apply_filter(pix, ideal_hp_filter, False)


def create_noncentered_ideal_high_pass(width, height, cutoff):
    # Not going to center the filter
    hp_filter = np.zeros((height, width))
    hp_filter.fill(1)
    for r in range(0, height):
        for c in range(0, cutoff - r):
            hp_filter[r, c] = 0
    return hp_filter


if __name__ == "__main__":
    high_pass_image(IMG_FILE)
    # Filter test
    #hp_filter = create_noncentered_ideal_high_pass(15, 15, 3)
    #print (hp_filter)
    #lp_filter = create_noncentered_ideal_low_pass(15, 15, 3)
    #print(lp_filter)