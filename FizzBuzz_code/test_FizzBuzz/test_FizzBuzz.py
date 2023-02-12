from FizzBuzz.FizzBuzz import FizzBuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_should_Fizz(self):
        x = 3
        expected_output = "Fizz"
        
        result = FizzBuzz(x)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_18_should_Fizz(self):
        x = 18
        expected_output = "Fizz"
        
        result = FizzBuzz(x)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_5_should_Buzz(self):
        x = 5
        expected_output = "Buzz"
        
        result = FizzBuzz(x)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_25_should_Buzz(self):
        x = 25
        expected_output = "Buzz"
        
        result = FizzBuzz(x)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_15_should_FizzBuzz(self):
        x = 15
        expected_output = "FizzBuzz"
        
        result = FizzBuzz(x)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_30_should_FizzBuzz(self):
        x = 30
        expected_output = "FizzBuzz"
        
        result = FizzBuzz(x)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_135_should_FizzBuzz(self):
        x = 135
        expected_output = "FizzBuzz"
        
        result = FizzBuzz(x)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    
        