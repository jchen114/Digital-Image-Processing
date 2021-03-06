IMAGE_FILE_NAME = 'Nintendo_image.jpg'
from PIL import Image
import os.path
from scipy.misc import toimage
import webbrowser
import numpy as np


def average_filter(img_file_name):
    # Open the image file and convert it to grayscale
    img = Image.open(img_file_name).convert('L')
    # Save the grayscale image into a file with png
    str_grey_file = os.path.splitext(os.path.basename(img_file_name))[0] + '.png'
    img.save(str_grey_file)
    # Display the grayscale file
    #webbrowser.open(str_grey_file)
    # Begin averaging over image
    # Build a 3 -by- 3 image filter, so each element is 1/9
    my_filter = 1.0/9.0 * np.ones(shape=(3, 3))
    # Convert image to numpy array for ease
    #print(my_filter)
    pix = np.asarray(img)
    #print('pix h: ' + str(pix.shape[0]) + ' w: ' + str(pix.shape[1]))
    # Apply the filter to the image
    filtered_img = apply_filter(pix, my_filter)
    toimage(filtered_img).show()


def apply_filter(img, some_filter):
    # Get the dimensions of the filter and the image
    filter_width = some_filter.shape[1]
    filter_height = some_filter.shape[0]
    img_width = img.shape[1]
    img_height = img.shape[0]
    # The size of the actual image without the buffer is then
    padded_img = np.lib.pad(img, 1, pad_with_zeros)
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
    average_filter(IMAGE_FILE_NAME)