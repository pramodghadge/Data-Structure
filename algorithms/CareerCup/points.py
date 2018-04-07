import math

class Point(object):
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def getDistence(self, point):
        return math.sqrt(math.pow(self.x - point.x, 2) + math.pow(self.y - point.y, 2))

    def isWithinDistance(self, point, distance):
        if abs(self.x - point.x) > distance or abs(self.y - point.y) > distance:
            return False

        return self.getDistence(point) <= distance