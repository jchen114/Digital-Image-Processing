# Digital-Image-Processing
Digital Image Processing class

CountRegions: 
Shades different coins with a different gray scale value. Each pixel belonging to a coin
should have the same gray scale value. 

Algorithm:
1. Iterate through pixels from top to bottom and alternating between left and right traversal.

2. Keep an array (called dist) detailing the last pixel that was seen belonging to a certain region.

3. For each pixel, determine whether it falls within a specified taxicab distance for each region.

4. If it does, then shade that pixel by the same grayscale value of that region and replace the dist
array with that value corresponding to the region.

5. If it does not, then make a new entry in the dist so that a new region will be added 

===============================================================================================

Invert Image: Inverts an image by applying a lambda function that inverts each pixel's RGB values
