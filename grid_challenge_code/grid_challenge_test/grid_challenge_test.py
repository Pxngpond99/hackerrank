from ..grid_challenge.grid_challenge import gridChallenge
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_give_ebacd_fghij_olmkn_trpqs_xywuv_should_YES(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_givekc_iu_should_YES(self):
        grid = ['kc','iu']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_uxf_vof_hmp_should_NO(self):
        grid = ['uxf', 'vof', 'hmp']
        expected_output = "NO"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_lyivr_jgfew_uweor_qxwyr_uikjd_should_NO(self):
        grid = ['lyivr', 'jgfew', 'uweor', 'qxwyr', 'uikjd']
        expected_output = "NO"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
    
    def test_give_nyx_ynx_xyt_should_YES(self):
        grid = ['nyx', 'ynx', 'xyt']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_zzzzzzzzzz_x10_YES(self):
        grid = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz','zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_tjxxx_xtxxj_rzzzz_zzrzz_rzzzz_should_YES(self):
        grid = ['tjxxx', 'xtxxj', 'rzzzz', 'zzrzz', 'rzzzz']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        