__author__ = 'Hooligan'
from PIL import Image
import os.path
from scipy.misc import toimage
import webbrowser
import numpy as np
IMAGE_FILE_NAME = 'Nintendo_image.jpg'


def laplacian_filter(img_file_name):
    img = Image.open(img_file_name).convert('L')
    str_grey_file = os.path.splitext(os.path.basename(img_file_name))[0] + '.png'
    img.save(str_grey_file)
    pix = np.asarray(img)
    laplace_filter = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    filtered_img = apply_filter(pix, laplace_filter)
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
    laplacian_filter(IMAGE_FILE_NAME)