__author__ = 'jacobchen2272'
from pymongo import MongoClient

class DBManager:

    client = None
    database = None
    descriptor_collection = None

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.database = self.client.descriptors_database
        self.descriptor_collection = self.database.SIFT

    def insert_kp_des(self, kps, des):

        for x in range(0, kps.length):
            kp = kps[x]
            des = des[x]
            sift_obj = {
                "keypoint": {
                    "angle": kp.angle,
                    "octave": kp.octave,
                    "point": (kp.pt[0], kp.pt[1]),
                    "response": kp.response,
                    "size": kp.size
                    },
                "descriptor":

                }

            self.descriptor_collection.insert_one(keypoint)

    def get_all_kps(self):
