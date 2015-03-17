## Equalization.py

main:
	Change the file here that you would like to perform histogram equalization on

histogram_equalization:
	1. Opens the image as greyscale image
	2. Gets the original histogram of the input (input_histogram)
	3. Calculates the CDF of the original image (cdf)
	4. Normalizes the CDF so that it can be used as a transform (normalize_cdf)
	5. Maps the pixel intensities from the image to the new image using the transform (transform_img)

input_histogram:
	1. Computes the histogram of the image by using a dictionary as the data structure
		The dictionary key is the intensity and the value is the amount of pixels with that intensity
	2. Plots the histogram
	3. Returns the histogram 

cdf:
	1. Orders the input dictionary so that the keys are sorted from least intensity to highest intensity
	2. Creates another ordered dictionary to be the CDF
	3. For each value in the input dictionary, it will add the previous entry of the CDF dictionary and the current value of the input dictionary
	
normalize_cdf:
	1. Normalizes the cdf so that it can be used as a transform
		Follows this equation: scaled_hist[k] = GRAYSCALE_MAX_LEVEL * (v - min_hist_value) / (img_size - min_hist_value) 
												where 
													v is the current value of the intensity
													min_hist_value is the value of the lowest intensity
													img_size is the complete size of the image
													GRAYSCALE_MAX_LEVEL is the maximum gray scale value allowed

transform_img:
	1. Maps the original image pixel values to the new image value via the normalized cdf
	2. Creates a new image from the mapping
	3. Plots the resulting histogram
	

Discussion:
	The resulting equalized images appear similar after running it on low contrast, low brightness, high contrast, and high brightness versions of the original image.
	I am curious as to why the high brightness image, high contrast image, and low brightness image histogram plots appear similar to each other while the low_contrast image
	histogram plot looks different from the rest. 
	There are differences between the histogram plots of the before and after comparisons, so I know that the plots are different
	from each other.
	These equalized histograms do correspond to the equalized images and they do appear similar as shown in the file displaying all the equalized images.