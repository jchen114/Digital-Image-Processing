__author__ = 'Hooligan'
from PIL import Image
import os.path
from scipy.misc import toimage
import numpy as np
IMAGE_FILE_NAME = 'Nintendo_image.jpg'


def sobel_filter_x(img):
    filter_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    filtered_img = apply_filter(img, filter_x)
    print("Print x filter")
    toimage(filtered_img).show()


def sobel_filter_y(img):
    filter_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    filtered_img = apply_filter(img, filter_y)
    print("Print y filter")
    toimage(filtered_img).show()


def sobel_filter_xy(img):
    filter_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    filter_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    filtered_img = apply_filter(img, filter_x)
    filtered_img = apply_filter(filtered_img, filter_y)
    print("Print x then y filter")
    toimage(filtered_img).show()


def apply_filter(img, some_filter):
    # Get the dimensions of the filter and the image
    filter_width = some_filter.shape[1]
    filter_height = some_filter.shape[0]
    img_width = img.shape[1]
    img_height = img.shape[0]
    # The size of the actual image without the buffer is then
    padded_img = np.lib.pad(img, int(filter_width/2), pad_with_zeros)
    filtered_img = np.empty([img_height, img_width])
    # Iterate through the image to get the submatrices to apply the filter on
    for r in range(0, img_height):
        for c in range(0, img_width):
            # Get the submatrix
            sub_matrix = padded_img[r:r+filter_height, c:c+filter_width]
            #print(sub_matrix)
            result_matrix = np.multiply(sub_matrix, some_filter)
            #print result
            #print("r : " + str(r) + " c: " + str(c))
            result = np.sum(result_matrix)
            filtered_img[r, c] = result
    return filtered_img


def pad_with_zeros(vector, pad_width, iaxis, kwargs):
    vector[:pad_width[0]] = 0
    vector[-pad_width[1]:] = 0
    return vector

if __name__ == "__main__":
    img = Image.open(IMAGE_FILE_NAME).convert('L')
    str_grey_file = os.path.splitext(os.path.basename(IMAGE_FILE_NAME))[0] + '.png'
    img.save(str_grey_file)
    pix = np.asarray(img)
    sobel_filter_x(pix)
    sobel_filter_y(pix)
    sobel_filter_xy(pix)