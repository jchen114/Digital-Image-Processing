__author__ = 'Hooligan'
import numpy as np
from scipy.misc import toimage
from PIL import Image

img_file_name = "Nintendo_Characters.jpg"


def center_filter(a_filter):
    # Centering the frequency
    top_left = a_filter
    top_left = np.fliplr(np.flipud(top_left))
    top_right = a_filter
    top_right = np.flipud(top_right)
    bottom_left = a_filter
    bottom_left = np.fliplr(bottom_left)
    bottom_right = a_filter

    top_hp_filter = np.concatenate((top_left, top_right), axis=1)
    bottom_hp_filter = np.concatenate((bottom_left, bottom_right), axis=1)

    some_filter = np.concatenate((top_hp_filter, bottom_hp_filter), axis=0)
    return some_filter


def apply_filter(pix, a_filter, centered):
    img_width = pix.shape[1]
    img_height = pix.shape[0]
    padded_img = np.zeros((2*img_height, 2*img_width))
    for h in range(0, img_height):
        for c in range(0, img_width):
            padded_img[h, c] = pix[h, c]
    ft = np.fft.fft2(padded_img)
    fshift = np.fft.fftshift(ft)
    # Display the magnitude spectrum
    #magnitude_spectrum = 20*np.log(np.abs(fshift))
    #toimage(magnitude_spectrum).show()
    # Apply filter here
    #toimage(a_filter * 255).show()
    if not centered:
        a_filter = center_filter(a_filter)
    fshift = fshift * a_filter
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    toimage(img_back).show()


if __name__ == "__main__":
    img = Image.open(img_file_name).convert('L')
    pix = np.asarray(img, None)
    #apply_filter(pix)