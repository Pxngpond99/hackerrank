from ..two_characters.two_characters import alternate
import unittest

class TwoCharatersTest(unittest.TestCase):
    def test_give_beabeefeab_should_5(self):
        s = "beabeefeab"
        expected_output = 5
        
        result = alternate(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_a_should_0(self):
        s = "a"
        expected_output = 0
        
        result = alternate(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
    
    def test_give_ab_should_2(self):
        s = "ab"
        expected_output = 2
        
        result = alternate(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
    
    def test_give_aaaaa_should_0(self):
        s = "aaaaa"
        expected_output = 0
        
        result = alternate(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_uyetuppelecb_should_0(self):
        s = "uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon"
        expected_output = 0
        
        result = alternate(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_cwomzxmuelma_should_8(self):
        s = "cwomzxmuelmangtosqkgfdqvkzdnxerhravxndvomhbokqmvsfcaddgxgwtpgpqrmeoxvkkjunkbjeyteccpugbkvhljxsshpoymkryydtmfhaogepvbwmypeiqumcibjskmsrpllgbvc"
        expected_output = 8
        
        result = alternate(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_asdcbsdcagfsdbgdfanfghbsfdab_should_8(self):
        s = "asdcbsdcagfsdbgdfanfghbsfdab"
        expected_output = 8
        
        result = alternate(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        