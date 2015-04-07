__author__ = 'jacobchen2272'
from PIL import Image
import numpy as np

IMG_DFT = "2D_DFT_LOG.png"
IMG_FFT_NUMPY = "FFT_Numpy.png"


def diff(img_1, img_2):
    img_1 = Image.open(img_1).convert('L')
    img_2 = Image.open(img_2).convert('L')

    pix_1 = np.asarray(img_1)
    pix_2 = np.asarray(img_2)

    diff = pix_2 - pix_1
    mag = np.abs(diff)
    print('biggest difference = ' + str(np.amax(mag)))

if __name__ == "__main__":
    diff(IMG_DFT, IMG_FFT_NUMPY)
