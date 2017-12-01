class Pet(object):
    no_of_pets = 0

    def __init__(self, name=None):
        self.name = name
        Pet.no_of_pets += 1

    def speak(self):
        print("My name's %s and the number of pets is %d" % (self.name, self.no_of_pets))


if __name__ == '__main__':
    p1 = Pet('rover')
    p1.speak()
    p2 = Pet('spot')
    p2.speak()
    p3 = Pet('cat')
    p3.speak()