__author__ = 'Hooligan'
IMAGE_FILE_NAME = 'Nintendo_image.jpg'
from PIL import Image
import os.path
import math
from scipy.misc import toimage
import webbrowser
import numpy as np


def median_filter(img_file_name):
    img = Image.open(img_file_name).convert('L')
    str_grey_file = os.path.splitext(os.path.basename(img_file_name))[0] + '.png'
    img.save(str_grey_file)
    pix = np.asarray(img)
    filtered_img = apply_median_filter(pix, 5)
    toimage(filtered_img).show()


def apply_median_filter(img, size):
    padding_length = int(size/2)
    padded_img = np.lib.pad(img, padding_length, pad_with_zeros)
    img_width = img.shape[1]
    img_height = img.shape[0]
    filter_height = int(size/2)
    filter_width = filter_height
    filtered_img = np.empty([img_height, img_width])
    for r in range(0, img_height):
        for c in range(0, img_width):
             # Get the submatrix
            sub_matrix = padded_img[r:r+filter_height, c:c+filter_width]
            median = np.median(sub_matrix)
            filtered_img[r, c] = median
    return filtered_img


def pad_with_zeros(vector, pad_width, iaxis, kwargs):
    vector[:pad_width[0]] = 0
    vector[-pad_width[1]:] = 0
    return vector

if __name__ == "__main__":
   median_filter(IMAGE_FILE_NAME)