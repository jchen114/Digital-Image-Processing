__author__ = 'jacobchen2272'
from Final_Project.SIFT_Descriptors.SIFT_DatabaseManager import DatabaseManager as dbm
from sklearn.decomposition import PCA
import pylab as pl
import matplotlib.pyplot as plt
import cv2


def cluster_sift_objects():
    db_manager = dbm.DBManager()
    (kps, dess) = db_manager.get_all_sift_objects()
    # Perform PCA to reduce dimensions to 2 and plot
    pca = PCA(n_components=2)
    pca.fit(dess)
    dess_reduced = pca.transform(dess)
    plt.scatter(dess_reduced[:,0], dess_reduced[:,1])
    plt.show()


if __name__ == "__main__":
    cluster_sift_objects()