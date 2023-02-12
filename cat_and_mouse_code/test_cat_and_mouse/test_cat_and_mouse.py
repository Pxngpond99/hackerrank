from cat_and_mouse.cat_and_mouse import catAndMouse
import unittest

class CatAndMouseTest(unittest.TestCase):
    def test_give_1_2_3_should_cat_b(self):
        # arrange
        cat_a = 1
        cat_b = 2
        mouse_c  = 3
        expected_output = 'Cat B'
        
        # act
        result = catAndMouse(cat_a, cat_b,mouse_c)
        # assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
    
    def test_give_1_5_3_should_mouse_c(self):
        cat_a = 1
        cat_b = 5
        mouse_c  = 3
        expected_output = 'Mouse C'
        
        result = catAndMouse(cat_a, cat_b,mouse_c)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_10_10_33_should_mouse_c(self):
        cat_a = 10
        cat_b = 10
        mouse_c  = 33
        expected_output = 'Mouse C'
        
        result = catAndMouse(cat_a, cat_b,mouse_c)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_del10_10_0_should_mouse_c(self):
        cat_a = -10
        cat_b = 10
        mouse_c  = 0
        expected_output = 'Mouse C'
        
        result = catAndMouse(cat_a, cat_b,mouse_c)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_10_20_20_should_cat_b(self):
        cat_a = 10
        cat_b = 20
        mouse_c  = 20
        expected_output = 'Cat B'
        
        result = catAndMouse(cat_a, cat_b,mouse_c)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_50_55_45_should_cat_a(self):
        cat_a = 50
        cat_b = 55
        mouse_c  = 45
        expected_output = 'Cat A'
        
        result = catAndMouse(cat_a, cat_b,mouse_c)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_50_100_del30_should_cat_a(self):
        cat_a = 50
        cat_b = 100
        mouse_c  = -30
        expected_output = 'Cat A'
        
        result = catAndMouse(cat_a, cat_b,mouse_c)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
        
    