import math


class Calculator(object):
    def add(self, a,b):
        return map(lambda x,y:x+y, a,b)

    def subtract(self, a,b):
        return map(lambda x, y: x - y, a, b)

    def multiply(self, a,b):
        return map(lambda x, y: x * y, a, b)

    def divide(self, a,b):
        if y == 0:
            return 'NaN'
        else:
            return map(lambda x, y: x / y, a, b)

    def exponent(self, a,b):
        return map(lambda x, y: x**y, a, b)

    def sqrt(self, a):
        return map(lambda x: x*0.5, a)

    def square(self, a):
        return list(map(lambda x: x*x, a))

    def cube(self, a):
        return map(lambda x: x**3, a)

    def sin(self, a):
        return map(lambda x: math.sin(x), a)

    def factorial(self, a):
       return reduce(lambda x: x * y, [1] + range(1, a + 1))

