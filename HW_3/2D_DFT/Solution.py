__author__ = 'Hooligan'
from PIL import Image
import numpy as np
import os.path
from scipy.misc import toimage
import cmath
import time
import math

IMAGE_FILE_NAME = 'Nintendo_Characters.jpg'


def two_d_dft(img_file_name):
    img = Image.open(img_file_name).convert('L')
    str_grey_file = os.path.splitext(os.path.basename(img_file_name))[0] + '.png'
    img.save(str_grey_file)
    pix = np.asarray(img)
    img_width = pix.shape[1]
    img_height = pix.shape[0]
    fft_result = np.empty([img_height, img_width])
    # M = img_height, N = img_width
    for r in range(0, img_height):
        for c in range(0, img_width):
            # F(u,v) = 1/(MN) * result
            value = (frequency_transform(r, c, img_width, img_height, pix))
            fft_result[r, c] = value
    # Normalizing to be 0 - 255
    #interval = float(np.amax(fft_result) - np.amin(fft_result))
    #fft_result = (fft_result - np.amin(fft_result))/interval * 255
    # Apply Natural Log for comparison with FFT (not sure why?)
    fft_result = 20*np.log(fft_result)
    toimage(fft_result).show()


def frequency_transform(u, v, img_width, img_height, img):
    value = 0
    # result = sum_(x=0,M-1){sum_(y=0,N-1){f(x,y)*exp(-j*2*pi*(u*x/M + v*y/N))}}
    for r in range(0, img_height):
        for c in range(0, img_width):
            # r = y, c = x
            value += img[r, c] * cmath.exp(-2j*(u*c/img_width + v*r/img_height))
    value = np.abs(value) # Power spectrum
    return value

if __name__ == "__main__":
    time_start = time.clock()
    two_d_dft(IMAGE_FILE_NAME)
    time_end = time.clock()
    print('time difference = ' + str(time_end - time_start))