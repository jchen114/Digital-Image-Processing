__author__ = 'Hooligan'
IMG_1 = 'Nintendo_Characters_1.jpg'
IMG_2 = 'Nintendo_Characters_2.jpg'
from PIL import Image
import os.path
import numpy as np
from scipy.misc import toimage


def fft_assignment(img_1, img_2):
    # Open up images
    img1 = Image.open(img_1).convert('L')
    img2 = Image.open(img_2).convert('L')
    str_grey_file_1 = os.path.splitext(os.path.basename(img_1))[0] + '.png'
    str_grey_file_2 = os.path.splitext(os.path.basename(img_2))[0] + '.png'
    img1.save(str_grey_file_1)
    img2.save(str_grey_file_2)
    # Fourier transforms
    print('Fourier transforms of images, shifted in freq domain')
    f1 = np.fft.fft2(img1)
    f1_shift = np.fft.fftshift(f1)
    f2 = np.fft.fft2(img2)
    f2_shift = np.fft.fftshift(f2)
    # Display Amplitude
    print('Display amplitude')
    # Get the amplitude
    f1_ampl = np.abs(f1_shift)
    f2_ampl = np.abs(f2_shift)
    display(f1_ampl)
    display(f2_ampl)
    # Display phase angle
    print('Display phases')
    # Get the phases
    f1_phase = f1 / np.absolute(f1)
    f2_phase = f1 / np.absolute(f2)
    display_phase(f1_phase)
    display_phase(f2_phase)
    # Display the image normally
    print('Reconstruct image normally')
    img1_reconstructed = np.fft.ifft2(f1)
    img2_reconstructed = np.fft.ifft2(f2)
    toimage(np.real(img1_reconstructed)).show()
    toimage(np.real(img2_reconstructed)).show()
    # Reconstruct image from amplitude
    print('Reconstruct image with amplitude')
    temp1 = np.nan_to_num(np.round(20*np.log(np.real(np.fft.ifft2(np.abs(f1))))))
    temp2 = np.nan_to_num(np.round(20*np.log(np.real(np.fft.ifft2(np.abs(f2))))))
    toimage(temp1).show()
    toimage(temp2).show()
    # Reconstruct image from phase
    print('Reconstruct image with phase')
    toimage(np.real(np.fft.ifft2(f1_phase))).show()
    toimage(np.real(np.fft.ifft2(f2_phase))).show()
    # Reconstruct first image with phase of second
    print('Reconstruct 1st image with phase of second')
    f1_swap = np.multiply(f1_ampl, f2_phase)
    toimage(np.real(np.fft.ifft2(f1_swap))).show()
    # Reconstruct second image with phase of first
    print('Reconstruct 2nd image with phase of first')
    f2_swap = np.multiply(f2_ampl, f1_shift)
    toimage(np.real(np.fft.ifft2(f2_swap))).show()


def display_phase(phase):
    toimage(normalize(np.angle(phase))).show()


def normalize(arr):
    interval = np.amax(arr) - np.amin(arr)
    normalized = (arr - np.amin(arr))/float(interval) * 255
    return normalized


def display(fft):
    real_spectrum = 20*np.log(fft)
    toimage(real_spectrum).show()

if __name__ == "__main__":
    fft_assignment(IMG_1, IMG_2)