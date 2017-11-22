import nxt

class HardwareMap(object):
    DEVICES = []

    def __init__(self,map):
        for port in map:
            for sensor in port:
                
