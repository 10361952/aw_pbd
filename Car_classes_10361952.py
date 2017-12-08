# Set up a Car class and give it attributes

class Car(object):
    # implement the car object.
#construct method the same for ever class
    def __init__(self):
#dodala type
        self.__type = ''
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = ''
 # dodala type (set + get)
    def getType(self):
        return self.__type

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage
    
    def setType(self, type):
        self.__type = type

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage


#engine size


    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage


# class thet transforms another class
class ElectricCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells (self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells

#adding classes for 3 missing types of cars

class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value        


class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1
        self.__NumberFuelCells = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value
        
    def getNumberFuelCells(self):
        return self.__NumberFuelCells

    def setNumberFuelCells (self, NumberFuelCells):
        self.__NumberFuelCells = NumberFuelCells
        
class PetrolCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value


# School notes - fleet of 40 cars (4 car options)
class CarFleet(object):
    def __init__(self):
        self.__cars = []
        self.__numAvailable = 40
        self.__profit = 0.0

    def getProfit(self):
        return self.__profit

    def getNumAvailable(self):
        return self.__numAvailable

    def rentCar(self, numCars):
        self.__numAvailable -= numCars
        self.__profit += (numCars * 20)
        print('Profit ' + str(self.__profit))
        print('Available ' + str(self.__numAvailable))

    def returnCar(self, numCars):
        self.__numAvailable += numCars
        print('Available ' + str(self.__numAvailable))



