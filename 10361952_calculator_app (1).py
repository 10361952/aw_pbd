# reference to file with classess and definition 
from Aga_Calculator_classes Calculator
import math

# definition to pull raw input from the user and depending on the operation - callll

def calculate():
    # raw input for user to type i
    try:
        x = float(raw_input('Please enter the first number: '))
        number_2 = raw_input('Would you like to input second number? Y or N?')
        if number_2 == "Y":
            y = float(raw_input('Please enter the second number: '))
        operation = raw_input('What would you like to do? Etc. add, multiply, subtract?')
    except:
        print
        "Input must be correct - try again"

    if number_2 == "Y" and operation == "add":
        print('{} + {} = '.format(x, y))
        print(Calculator.add(Calculator, x, y))

    elif number_2 == "Y" and operation == 'subtract':
        print('{} - {} = '.format(x, y))
        print(Calculator.subtract(Calculator, x, y))

    elif number_2 == "Y" and operation == 'multiply':
        print('{} * {} = '.format(x, y))
        print(Calculator.multiply(Calculator, x, y))

    elif number_2 == "Y" and operation == 'divide':
        print('{} / {} = '.format(x, y))
        print(Calculator.divide(Calculator, x, y))

    elif number_2 == "Y" and operation == 'exponent':
        print('{} ** {} = '.format(x, y))
        print(Calculator.exponent(Calculator, x, y))

    elif number_2 == "N" and operation == 'sqrt':
        print('{} = '.format(x))
        print(Calculator.sqrt(Calculator, x))

    elif number_2 == "N" and operation == 'square':
        print('{} = '.format(x))
        print(Calculator.square(Calculator, x))

    elif number_2 == "N" and operation == 'cube':
        print('{} = '.format(x))
        print(Calculator.cube(Calculator, x))

    elif number_2 == "N" and operation == 'sin':
        print('{} = '.format(x))
        print(Calculator.sin(Calculator, x))

    elif number_2 == "N" and operation == 'factorial':
        print('{} = '.format(x))
        print(Calculator.factorial(Calculator, x))

    else:
        print('Please type a valid operator!')


# definiotion to give a user chance to perform another calculation
def again():
    calc_again = raw_input('Would you like to continue? Y/N')

    if calc_again == 'Y':
        calculate()
    elif calc_again == 'N':
        print('See you later.')
    else:
        print("Wrong input - type Y  or N")
        again()


calculate()
again()