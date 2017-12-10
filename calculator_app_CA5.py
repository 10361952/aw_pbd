# reference to file with classess and definition
import math
from calculator_classes import Calculator

#code made in a new version of Python - instead or raw_input we have just inputs
#definition to change elements of the lists into a float
def intinate(lis):
    array_length = len(lis)
    for i in range(array_length):
        z = float(lis[i])
        lis[i] = z
    return lis

def calculate():
    try:
        # raw input from user
        a = intinate(input('Please enter the first list of numbers on which you would like to compute: ').split(","))
        number_2 = input('Would you like to input second list? Y or N?')
        if number_2 == "Y":
            b = intinate(input('Please enter the second list of numbers: ').split(","))
        operation = input('What would you like to do? Etc. add, multiply, subtract?')
    except:
        print("Input must be correct - try again")

    if number_2 == "Y" and operation == "add":
        print('{} + {} = '.format(a, b))
        print(Calculator.add(Calculator, a, b))

    elif number_2 == "Y" and operation == 'subtract':
        print('{} - {} = '.format(a, b))
        print(Calculator.subtract(Calculator, a,b))

    elif number_2 == "Y" and operation == 'multiply':
        print('{} * {} = '.format(a,b))
        print(Calculator.multiply(Calculator, a,b))

    elif number_2 == "Y" and operation == 'divide':
        print('{} / {} = '.format(a,b))
        print(Calculator.divide(Calculator, a,b))

    elif number_2 == "Y" and operation == 'exponent':
        print('{} ** {} = '.format(a,b))
        print(Calculator.exponent(Calculator, a,b))

    elif number_2 == "N" and operation == 'sqrt':
        print('{} = '.format(a))
        print(Calculator.sqrt(Calculator, a))

    elif number_2 == "N" and operation == 'square':
        print('{} = '.format(a))
        print(Calculator.square(Calculator, a))

    elif number_2 != "N" and operation == 'cube':
        print('{} = '.format(a))
        print(Calculator.cube(Calculator, a))

    elif number_2 == "N" and operation == 'sin':
        print('{} = '.format(a))
        print(Calculator.sin(Calculator, a))

    elif number_2 == "N" and operation == 'factorial':
        print('{} = '.format(a))
        print(Calculator.factorial(Calculator, a))

    else:
        print('Please type a valid operator!')


# definiotion to give a user chance to perform another calculation
def again():
    calc_again = input('Would you like to continue? Y/N')

    if calc_again == 'Y':
        calculate()
    elif calc_again == 'N':
        print('See you later.')
    else:
        print("Wrong input - type Y  or N")
        again()


calculate()
again()