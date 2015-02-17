__author__ = 'jacobchen2272'
from PIL import Image
import webbrowser
import collections
import os.path
import matplotlib.pyplot as plt

GRAYSCALE_MAX_LEVEL = 255


def histogram_equalization(str_file):
    img = Image.open(str_file).convert('LA')
    str_grey_file = os.path.splitext(os.path.basename(str_file))[0] + '.png'
    img.save(str_grey_file)
    webbrowser.open(str_grey_file)
    i_hist = input_histogram(img)
    cdf_hist = cdf(i_hist)
    scaled_hist = normalize_cdf(cdf_hist, img)
    transform_img(img, scaled_hist, str_file)


def input_histogram(img):
    pix = img.load()
    (w, h) = img.size
    # put into histogram dictionary
    histogram = dict()
    for r in range(0, h):
        for c in range(0, w):
            # check if intensity exists
            intensity = pix[c, r][0]
            if intensity in histogram:
                histogram[intensity] += 1
            else:
                histogram[intensity] = 1
    
    plt.bar(range(len(histogram)), histogram.values(), align='center')
    plt.xticks(range(len(histogram)), histogram.keys())
    plt.show()
    return histogram


def cdf(hist):
    ordered_intensities = collections.OrderedDict(sorted(hist.items()))
    cdf_dict = collections.OrderedDict()
    minimum_intensity = ordered_intensities.popitem(last=False)
    cdf_dict.update({minimum_intensity[0]: minimum_intensity[1]})
    for k, v in ordered_intensities.items():
            cdf_dict[k] = ordered_intensities[k] + cdf_dict[next(reversed(cdf_dict))]   # Add current value to the previous one
    return cdf_dict


def normalize_cdf(cdf_hist, img):
    (w, h) = img.size
    img_size = w*h
    min_hist_value = cdf_hist.items()[0][1]
    scaled_hist = dict()
    for k, v in cdf_hist.items():
        scaled_hist[k] = GRAYSCALE_MAX_LEVEL * (v - min_hist_value) / (img_size - min_hist_value)
    #scaled_hist = {k: (v - min_hist_value) / (img_size - min_hist_value) * GRAYSCALE_MAX_LEVEL for k, v in cdf_hist.items()}
    return scaled_hist


def transform_img(img, scaled_hist, str_file):
    #   Map the pixels from the image to the new image
    pix = img.load()
    (w, h) = img.size
    eq_img = Image.new('L', (w, h), 0)
    eq_pix = eq_img.load()
    
    for r in range(0, h):
        for c in range(0, w):
            intensity = pix[c, r][0]
            eq_pix[c, r] = scaled_hist[intensity]
            
    histogram = dict()    
    # Plot the new image histogram    
    for r in range(0, h):
        for c in range(0, w):
            intensity = eq_pix[c, r]
            if intensity in histogram:
                histogram[intensity] += 1
            else:
                histogram[intensity] = 1
    
    new_img_loc = os.path.splitext(os.path.basename(str_file))[0] + '-equalized.png'
    eq_img.save(new_img_loc)
    webbrowser.open(new_img_loc)
    plt.bar(range(len(histogram)), histogram.values(), align='center')
    plt.xticks(range(len(histogram)), histogram.keys())
    plt.show()

if __name__ == "__main__":
    histogram_equalization('./low_contrast_image.jpg')
    # args = sys.argv[1:]
    # try:
    #     if len(args > 2) or len(args < 1):
    #         raise Exception('Input one file')
    #     str_file = args[0]
    #     if str_file.lower().endswith('.png', '.jpg', '.jpeg'):
    #         histogram_equalization(str_file)
    #     else:
    #         raise Exception('.png, .jpg, .jpeg only please')
    # except Exception, e:
    #     print(e.message)