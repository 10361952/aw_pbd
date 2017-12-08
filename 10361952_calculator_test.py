import unittest

from calculator import Calculator 

# test the calculator functionality
class TestCalculator(unittest.TestCase):
 
    def setUp(self):
        self.calc = Calculator()
 
# this tests the add functionality
# 2 + 2 = 4
# 2 + 4 = 6
# 2 + (-2) = 0
    def test_calculator_add(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)
 
    def test_calculator_subtract(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)
        
    def test_calculator_multiply(self):
        result = self.calc.multi(2,5)
        self.assertEqual(10, result)
        result = self.calc.multi(3,7)
        self.assertEqual(21, result)
        result = self.calc.multi(8,5)
        self.assertEqual(40, result)

    def test_calculator_division(self):
        result = self.calc.div(5,5)
        self.assertEqual(1, result)
        result = self.calc.div(30,6)
        self.assertEqual(5, result)
        result = self.calc.div(80,10)
        self.assertEqual(8, result)

    def test_calculator_exponent(self):
        result = self.calc.expo(3,3)
        self.assertEqual(27, result)
        result = self.calc.expo(5,4)
        self.assertEqual(625, result)
        result = self.calc.expo(15,6)
        self.assertEqual(11390625, result)        
		
	def test_calculator_square(self):
        result = Calculator().square(7)
        self.assertEqual(49,result)
        result = Calculator().square(-8)
        self.assertEqual(64, result)

		
	def test_calculator_sqrt(self):
        result  = Calculator().sqrt(64)
        self.assertEqual(8,result)
        result  = Calculator().sqrt(-100)
        self.assertEqual('NaN',result)
        result  = Calculator().sqrt(0)
        self.assertEqual('NaN',result)
        result  = Calculator().sqrt(81.6)
        self.assertEqual(9.033271832508971,result) 

    def test_calculator_cube(self):
        result = self.calc.cbe(10)
        self.assertEqual(1000, result)
        result = Calculator().cube(-3)
        self.assertEqual(-27,result)
        result = self.calc.cbe(9)
        self.assertEqual(729, result)
 

    def test_calculator_sin(self):
        result = self.calc.sin(68)
        self.assertAlmostEqual(-0.897927680689, result)
        result = Calculator().sin(0)
        self.assertEqual(0)
        result = self.calc.sin(23)
        self.assertAlmostEqual(-0.846220404175, result)        
               
	def test_calculator_factorial(self):
        result = Calculator().factorial(4)
        self.assertEqual(24, result)
        result = Calculator().factorial(-8)
        self.assertEqual('Factorial of negative numbers does not exist', result)
        result = Calculator().factorial(0)
        self.assertEqual('Factorial of 0 equals 1', result)


    
if __name__ == '__main__':
    unittest.main()