__author__ = 'jacobchen2272'


class K_Means:

    cluster_centers = None
    prediction_labels = None

    def __init__(self, centers, predictions):
        self.cluster_centers = centers
        self.prediction_labels = predictions