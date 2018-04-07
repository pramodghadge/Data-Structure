class Car(object):
    def __repr__(self, wheels=4, color='Green', seats=4):
        self.wheels = wheels
        self.color  = color
        self.seats = seats

    def __repr__(self):
        return 'Car is {0}, has {1} wheels and {2} seats,name:{3}.'.format(
            self.color,
            self.wheels,
            self.seats,
            self.__class__.__name__
        )


from abc import ABCMeta, abstractmethod

class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def setColor(self):
        pass

    @abstractmethod
    def setWheels(self):
        pass

    @abstractmethod
    def setSeats(self):
        pass

    @abstractmethod
    def getResults(self):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def setColor(self, color):
        self.car.color = color

    def setWheels(self, wheels):
        self.car.wheels = wheels

    def setSeats(self, seats):
        self.car.seats = seats

    def getResults(self):
        return self.car


class CarBuilderDirector(object):
    @staticmethod
    def getCar():
        car = CarBuilder()
        car.setWheels(4)
        car.setColor('Red')
        car.setSeats(4)
        return car.getResults()

if __name__ == '__main__':
    car = CarBuilderDirector.getCar()
    print car