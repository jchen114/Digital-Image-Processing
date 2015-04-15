__author__ = 'jacobchen2272'


class Keypoint:

    angle = None
    octave = None
    pt = None
    response = None
    size = None

    def __init__(self, angle, octave, pt, response, size):
        self.angle = angle
        self.octave = octave
        self.pt = pt
        self.response = response
        self.size = size