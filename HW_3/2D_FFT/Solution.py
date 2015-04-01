__author__ = 'Hooligan'
IMAGE_FILE_NAME = 'Nintendo_Characters.png'
import numpy as np
from PIL import Image
from scipy.misc import toimage
import time


def fft(img_file_name):
    img = Image.open(img_file_name).convert('L')
    f = np.fft.fft2(img)

    real_spectrum = 20*np.log(np.abs(f))
    # Normalization
    #(width, height) = img.size
    #real_spectrum = 1/float(width * height) * np.abs(f)
    #interval = np.amax(real_spectrum) - np.amin(real_spectrum)
    #real_spectrum = (real_spectrum - np.amin(real_spectrum))/float(interval) * 255
    toimage(real_spectrum).show()


if __name__ == "__main__":
    time_begin = time.clock()
    fft(IMAGE_FILE_NAME)
    time_end = time.clock()
    print('time difference = ' + str(time_end - time_begin))

