import unittest

from calculator import Calculator 


class Test_calculator(unittest.TestCase):
 
    def setUp(self):
        self.calc = Calculator()



    def test_calculator_add(self):
        result  = Calculator().add(5,5)
        self.assertEqual(10,result)
        result  = Calculator().add(2,3)
        self.assertEqual(5,result)
        result  = Calculator().add(2,0)
        self.assertEqual(2,result)
      
    def test_calculator_subtract(self):
        result  = Calculator().subtract(5,3)
        self.assertEqual(2,result)
        result  = Calculator().subtract(2,0)
        self.assertEqual(2,result)
        result  = Calculator().subtract(0,2)
        self.assertEqual(-2,result)
        
    def test_calculator_multiply(self):
        result  = Calculator().multiply(5,5)
        self.assertEqual(25,result)
        result  = Calculator().multiply(0,5)
        self.assertEqual(0,result)
        result  = Calculator().multiply(5,2)
        self.assertEqual(10,result)
        result  = Calculator().multiply(5,0.2)
        self.assertEqual(1,result)
        
    def test_calculator_divide(self):
        result  = Calculator().divide(5,5)
        self.assertEqual(1,result)
        result  = Calculator().divide(5,0)
        self.assertEqual('NaN',result)  #not a number
        result  = Calculator().divide(5,1)
        self.assertEqual(5,result)
        result  = Calculator().divide(10,2)
        self.assertEqual(5,result)
        result  = Calculator().divide(5,4)
        self.assertEqual(1.25,result)
        
    def test_calculator_exponent(self):
        result  = Calculator().exponent(5,2)
        self.assertEqual(25,result)
        result  = Calculator().exponent(5,0)
        self.assertEqual(1,result)
        result  = Calculator().exponent(0,2)
        self.assertEqual(0,result)
        result  = Calculator().exponent(-3,3)
        self.assertEqual(-27,result)  

    def test_calculator_sqrt(self):
        result  = Calculator().sqrt(16)
        self.assertEqual(4,result)
        result  = Calculator().sqrt(-100)
        self.assertEqual('NaN',result)
        result  = Calculator().sqrt(0)
        self.assertEqual('NaN',result)
        result  = Calculator().sqrt(81.6)
        self.assertEqual(9.033271832508971,result)        
    
    def test_calculator_square(self):
        result = Calculator().square(2)
        self.assertEqual(4,result)
        result = Calculator().square(-8)
        self.assertEqual(64, result)
        
    def test_calculator_cube(self): 
        result = Calculator().cube(3)
        self.assertEqual(27,result)
        result = Calculator().cube(-4)
        self.assertEqual(-64,result)

    def test_calculator_sin(self): 
        result = Calculator().sin(0)
        self.assertEqual(0)
        
    def test_calculator_factorial(self):
        result = Calculator().factorial(4)
        self.assertEqual(24, result)
        result = Calculator().factorial(-8)
        self.assertEqual('Factorial of negative numbers does not exist', result)
        result = Calculator().factorial(0)
        self.assertEqual('Factorial of 0 equals 1', result)

    
if __name__ == '__main__':
    unittest.main()
