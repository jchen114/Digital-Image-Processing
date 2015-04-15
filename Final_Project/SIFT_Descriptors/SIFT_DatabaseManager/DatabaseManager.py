__author__ = 'jacobchen2272'
import pymongo as pym
from pymongo import errors
from Final_Project.SIFT_Descriptors.Models import Keypoint as kpt
import numpy as np
import cv2


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

        for x in range(0, len(kps)):
            kp = kps[x]
            descriptor = des[x]
            sift_obj = {
                "keypoint": {
                    "angle": kp.angle,
                    "octave": kp.octave,
                    "point": {
                        'x': kp.pt[0],
                        'y': kp.pt[1]
                    },
                    "response": kp.response,
                    "size": kp.size
                },
                "descriptor": {
                    "data":str(descriptor)
                }
            }

            self.descriptor_collection.insert_one(sift_obj)

    def get_all_sift_objects(self):
        cursor = self.descriptor_collection.find()
        sift_objects = cursor[0:cursor.count()]
        kps = []
        dess = []
        for sift_object in sift_objects:
            keypoint = sift_object['keypoint']
            kp = kpt.Keypoint(keypoint['angle'], keypoint['octave'], (keypoint['point']['x'], keypoint['point']['y']), keypoint['response'], keypoint['size'])
            descriptor = sift_object['descriptor']['data']
            descriptor = descriptor[1:len(descriptor) - 2].replace(".", "")
            #print descriptor
            # turn descriptor into a numeric array
            des = [int(s) for s in descriptor.split()]
            dess.append(des)
            kps.append(kp)
        dess = np.matrix(dess)
        return kps, dess

    def delete_all_sift_objects(self):
        result = self.descriptor_collection.delete_many({})
        print 'Number of documents deleted = ' + str(result.deleted_count)

    def close(self):
        self.client.close()