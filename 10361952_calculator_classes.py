
import math

class Calculator(object):

    def checknumber(self, x, y):
        # function that checks that input fields are numeric
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return True
        else:
            return False
 
    def add(self, x, y):
        # add the two inputs together
        number_type = (int, float, complex)
        if isinstance(x,number_type) and isinstance(y,number_type):
            return x + y
        else:
            raise ValueError
            
    def subtract(self, x, y):
        # subtract the second number from the first
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError
        
    def multiply(self, x, y):
        #multiply inputs together
        if self.checknumber(self, x, y):
            return x * y
        else:
            raise ValueError
        
    def divide(self, x,y):
        #divide the second number into the first
        if self.checknumber(self, x, y):
            if y == 0:
                return 'NaN'
            else:
                return x / y
        else:
            raise ValueError
            
    def exponent(self, x,y):
        #the exponential of the first number to the power of the second
        if self.checknumber(self, x, y):
            return x**y
        else:
            raise ValueError
        
    def sqrt(self,x):
        #square root of the input number
        if x <=0:
            return ('NaN')
        else:
            return x**0.5
            
    def square (self, x):
        #square of the input number
        return x**2
        
    def cube (self, x):
        #cube of the input number
        return x**3
    
    
    def sin(self, x):
        #sine of the input number
        from math import sin
        try:
            return math.sin(x)
        except:
            raise ValueError
    
    def factorial(self, x):
        #factorial of the input number
        factorial = 1
        if x < 0:
            return ('Factorial of negative numbers does not exist')
        elif x == 0:
            return ('Factorial of 0 equals 1')
        else:
            for x in range (1, x+1):
                return math.factorial(x)
        

    
