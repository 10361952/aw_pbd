
from Car import *


#notes form class (cars in stockage)
class Dealership(object):
    def __init__(self):
        print("Hi there! Welcome to Aungier Car Rental, where we have 40 cars to rent out in 4 options: petrol, diesel, electric, hybrid cars.")
        # Initialize lists of car types (All empty at start)
        self.diesel_car = []
        self.electric_car = []
        self.hybrid_car = []
        self.petrol_car = []

    # Create 20 petrol, 8 diesel etc. cars and add to list
    def create_current_stock(self):
            for i in range(20):
               self.petrol_car.append(PetrolCar())
            for i in range(8):
               self.diesel_car.append(DieselCar())
            for i in range(8):
               self.hybrid_car.append(HybridCar())
            for i in range(4):
               self.electric_car.append(ElectricCar())

    # Returns how many cars available each type
    def stock_count(self):
        print ("Available cars are listed below:")
        print ("petrol cars in stock " + str(len(self.petrol_car)))
        print ('electric cars in stock ' + str(len(self.electric_car)))
        print ('diesel cars in stock ' + str(len(self.diesel_car)))
        print ('hybrid cars in stock ' + str(len(self.hybrid_car)))

    # Rent a car to someone CALLED BY BELOW
    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print ('Not enough cars in stock')
            return
        for i in range(amount):
            car_list.pop()

    # Return a car to someone CALLED BY BELOW
    def return_car(self, car_list, amount):
        for i in range(amount):
            car_list.append(Car())

    #defining examples of car object available for the end users to rent/return
    def define(self):
        # Create empty dictionary for values to fill
        examples = {}
        examples["diesel_car_1"] = DieselCar()
        assert isinstance(examples["diesel_car_1"], object)
        examples["diesel_car_1"].setType('Diesel')
        examples["diesel_car_1"].setColour('Green')
        examples["diesel_car_1"].setMake('Opel')
        examples["diesel_car_1"].move(30)

        examples["petrol_car_1"] = PetrolCar()
        assert isinstance(examples["petrol_car_1"], object)
        examples["petrol_car_1"].setType('Diesel')
        examples["petrol_car_1"].setColour('Black')
        examples["petrol_car_1"].setMake('Mercedes')
        examples["petrol_car_1"].move(120)

        examples["hybrid_car_1"] = HybridCar()
        assert isinstance(examples["hybrid_car_1"], object)
        examples["hybrid_car_1"].setType('Hybrid')
        examples["hybrid_car_1"].setColour('Pink')
        examples["hybrid_car_1"].setMake('Astra')
        examples["hybrid_car_1"].move(80)

        examples["electric_car_1"] = ElectricCar()
        assert isinstance(examples["electric_car_1"], object)
        examples["electric_car_1"].setType('Electric')
        examples["electric_car_1"].setColour('Silver')
        examples["electric_car_1"].setMake('Tesla')
        examples["electric_car_1"].move(30)
        # Return dictionary
        return examples


    # Choose to rent/return a car + options for car to rent
    def process_rental(self):
        option = input("Would you like to rent a car or return one? Just type RENT or RETURN")
        if option == "RENT" or "Rent":
            car_type = input("Which type of a car? Type diesel, petrol, electric or hybrid")
            amount = int(input("How many cars?"))
            # Defined values returned in dictionary
            examples = self.define()
            if car_type == "petrol" or "Petrol":
                #make it total - rent
                self.rent(self.petrol_car, amount)
                print('Description of the diesel car that is available: ')
                print('Colour: ', examples["petrol_car_1"].getColour())
                print('Type: ', examples["petrol_car_1"].getType())
                print('Make: ', examples["petrol_car_1"].getMake())
                print('Mileage: ', examples["petrol_car_1"].getMileage())
                #print('Engine size: ', examples["petrol_car_1"].getEngineSize())

            elif car_type == "diesel" or "Diesel":
                self.rent(self.diesel_car, amount)
                print(" Description of the diesel car that is available: ")
                print('Colour: ', examples["diesel_car_1"].getColour())
                print('Type: ', examples["diesel_car_1"].getType())
                print('Make: ', examples["diesel_car_1"].getMake())
                print('Mileage: ', examples["diesel_car_1"].getMileage())
                #print('Engine size: ', examples["diesel_car_1"].getEngineSize())

            elif car_type == "hybrid" or "Hybrid":
                self.rent(self.hybrid_car, amount)
                print("Description of the hybrid car that is available: ")
                print('Colour: ', examples["hybrid_car_1"].getColour())
                print('Type: ', examples["hybrid_car_1"].getType())
                print('Make: ', examples["hybrid_car_1"].getMake())
                print('Mileage: ', examples["hybrid_car_1"].getMileage())
                #print('Engine size: ', examples["hybrid_car_1"].getEngineSize())

            elif car_type == "electric" or "Electric":
                self.rent(self.electric_car, amount)
                print('Description of the electric car that is available:')
                print('Colour: ', examples["electric_car_1"].getColour())
                print('Type: ', examples["electric_car_1"].getType())
                print('Make: ', examples["electric_car_1"].getMake())
                print('Mileage: ', examples["electric_car_1"].getMileage())
                #print('Engine size: ', examples["electric_car_1"].getEngineSize())

        elif option == "RETURN" or "Return":
            car_type = input("Which type of a car? Type diesel, petrol, electric or hybrid")
            amount = int(input("How many cars?"))
            # make it total + return
            if car_type == "petrol" or "Petrol":
                self.return_car(self.petrol_car, amount)
                print ("Thank you for renting out with us!")
            elif car_type == "diesel" or "Diesel":
                self.return_car(self.diesel_car, amount)
                print("Thank you for renting out with us!")
            elif car_type == "hybrid" or "Hybrid":
                self.return_car(self.hybrid_car, amount)
                print("Thank you for renting out with us!")
            elif car_type == "electric" or "Electric":
                self.return_car(self.electric_car, amount)
                print("Thank you for renting out with us!")
            else:
                print("Sorry, input must be correct - try again")
        else:
            print("Sorry, input must be correct - try again")

#ending function

    def again(self):
        operation_again = input('Would you like to continue and make another query? Y/N')
        if operation_again == 'Y':
            self.process_rental()
        elif operation_again == 'N':
            print('See you later and have a nice day!')
        else:
            print("Wrong input - please type Y to continue or N to stop")
            self.again()
