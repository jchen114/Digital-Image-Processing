__author__ = 'jacobchen2272'
import pymongo as pym
from pymongo import errors


class DBManager:

    client = None
    database = None
    descriptor_collection = None

    def __init__(self, ip_addr='localhost', port=27017):
        try:
            self.client = pym.MongoClient(ip_addr, port)
            self.database = self.client.descriptors_database
            self.descriptor_collection = self.database.SIFT
        except errors.InvalidName as e:
            # Invalid collection name
            print(e)
            print 'Creating a new collection'
            self.database.create_collection('SIFT')

    def insert_kp_des(self, kps, des):

        for x in range(0, kps.length):
            kp = kps[x]
            descriptor = des[x]
            sift_obj = {
                "keypoint": {
                    "angle": kp.angle,
                    "octave": kp.octave,
                    "point": (kp.pt[0], kp.pt[1]),
                    "response": kp.response,
                    "size": kp.size
                },
                "descriptor": {
                    "data":descriptor
                }
            }

            self.descriptor_collection.insert_one(sift_obj)

    def get_all_sift_objects(self):
        sift_objects = self.descriptor_collection.find()
        kps = []
        dess = []
        for sift_object in sift_objects:
            keypoint = sift_object.keypoint
            descriptor = sift_object.descriptor
            kps.append(keypoint)
            dess.append(descriptor)
        return kps, dess

    def delete_all_sift_objects(self):
        self.descriptor_collection.delete_many()