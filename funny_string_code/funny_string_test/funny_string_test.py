from funny_string.funny_string import funnyString
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_give_acxz_should_Funny(self):
        s = "acxz"
        expected_output = "Funny"
        
        result = funnyString(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_bcxz_should_Not_Funny(self):
        s = "bcxz"
        expected_output = "Not Funny"
        
        result = funnyString(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_qvskvvqkkmdj_should_Not_Funny(self):
        s = "qvskvvqkkmdjouseikfeurwxjovvjxgbuxkqucceoenczhhhrlknegkpwfmheriyqrqltrojwdmvksedgorlvcztimbodimtbeetuteqypnkkqmrgdccgcwopwctgpmhsrconiglwsuiiibokdrqgngwmjprzcztuehhlmtjeprnwrbjvrbbhiwsqmlrplklqssbenjjdcxbtyjqrjrzqpridfytrkfhcyhhlrrntpqmpycgiugzmyiofiivsoctmkdwctmuiciwzlfjimltmujrcsovgqrrctofocyydiwevbpdozvbvetyyhueynvbilfvogtqpqvksmmhnjjipchnkdqjrnjyzptnwpfohbxbomhcwrjlurzftsnmhxkhogtnubbddzdqlmrkdb"
        expected_output = "Not Funny"
        
        result = funnyString(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_xskqyrzyuzxr_should_Funny(self):
        s = "xskqyrzyuzxrxpwqunumoumswqvqstwsxzyumnruztlnszskpuntvptzwoqumqyuzryumpvzrwrvyvyqxytuowqrzswpruxruvwyvpvxzxsxszvyrzwrzrwpvnszwptyquoqruyvqyrszxuzystlqvpsxuvopuxpxprsvqtmqrywyzsuovxuyrwopuoqrzyzsuvwqtmorwzvpqvyqwqyvqpvzwromtqwvuszyzrqoupowryuxvouszywyrqmtqvsrpxpxupovuxspvqltsyzuxzsryqvyurqouqytpwzsnvpwrzrwzryvzsxsxzxvpvywvurxurpwszrqwoutyxqyvyvrwrzvpmuyrzuyqmuqowztpvtnupkszsnltzurnmuyzxswtsqvqwsmuomunuqwpxrxzuyzrksyql"
        expected_output = "Funny"
        
        result = funnyString(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq_should_Funny(self):
        s = "ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq"
        expected_output = "Funny"
        
        result = funnyString(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_ivvkxq_should_Not_Funny(self):
        s = "ivvkxq"
        expected_output = "Not Funny"
        
        result = funnyString(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
    def test_give_jkmsxzwrxzy_should_Not_Funny(self):
        s = "jkmsxzwrxzy"
        expected_output = "Not Funny"
        
        result = funnyString(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
        
        