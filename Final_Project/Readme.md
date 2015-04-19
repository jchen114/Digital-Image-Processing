# Final Project for Digital Image Processing

## Goal

I would like to see if I could use SIFT descriptors described in the paper titled > Distinctive Image Features from Scale-Invariant Keypoints
to differentiate between the Mario Nintendo character and the Boo Nintendo Character.

## Methodology
-	Gather the SIFT descriptors and keypoints of several Mario images and removed the keypoints that were located in the background of the images
- 	Store the SIFT descriptors and keypoints in MongoDB so that I would not have to continuously compute them.
-	Perform PCA on the descriptors and plot them on their 2 principal components to see whether there are clusters of similar data.
-	Cluster the descriptors using k-means
-	Test the descriptors using pictures from Mario and Boo and determine the distances that set apart the characters.
-	Distances are calculated by taking the SIFT descriptor from each of the new images and finding the closest cluster they belong to. Then sum up all the distances.

## Discussion
Using the number of clusters as 7, we see that the Mario descriptors have a distance of above 100,000 and Boo below 100000.
This may be due to the fact that there are less descriptors of Boo than there are with Mario. The number of clusters was eye-balled to be around 7.
I only plotted them on their 2 most principal axis' and the clusters could be overlapping.

## Future Work
I may sweep the number of clusters to see which cluster number gives the best discrepancy between Mario descriptors and Boo descriptors. 
Also, I would like to resolve the problem that there may be varying number of descriptors for images that may need to be accounted for.