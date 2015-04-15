__author__ = 'jacobchen2272'
from Final_Project.SIFT_Descriptors.SIFT_DatabaseManager import DatabaseManager as dbm
from Final_Project.SIFT_Descriptors.Models import K_Means as km
from sklearn.decomposition import PCA
import pylab as pl
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import cv2


def cluster_sift_objects():
    db_manager = dbm.DBManager()
    (kps, dess) = db_manager.get_all_sift_objects()
    # Perform PCA to reduce dimensions to 2 and plot
    pca = PCA(n_components=2)
    pca.fit(dess)
    dess_reduced = pca.transform(dess)
    #plt.scatter(dess_reduced[:,0], dess_reduced[:,1])
    #plt.show()
    k_means = KMeans(n_clusters=5, random_state=0)  # Fixing the RNG in kmeans
    k_means.fit(dess)
    cluster_centers = k_means.cluster_centers_
    y_pred = k_means.predict(dess)
    pl.scatter(dess_reduced[:, 0], dess_reduced[:, 1], c=y_pred)
    pl.show()
    km_object = km.K_Means(cluster_centers, y_pred)
    return km_object


if __name__ == "__main__":
    cluster_sift_objects()