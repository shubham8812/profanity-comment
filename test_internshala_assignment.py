import internshala_assignment as intern
import unittest


class SimpleTest(unittest.TestCase):
    
    # returns True or False.
    def test_profanity(self): 
        self.assertEqual(intern.pro('fuck you asshole'),0.2)
        self.assertEqual(intern.pro('he is a bastard'),0.1)
        self.assertEqual(intern.pro('this is unittest for profanity'),0.0)
    
    
    
if __name__ == '__main__':
    unittest.main()


# go to command line and type python test_internshala_assignment.py -v
# if it is successful 'OK' message will occur
# if it fails assertion error will occur.

# test for 'fuck you asshole' failed, expected result was 0.2 and result was 0.3
# so i have to alter the code inside pro() function, i eliminated the if statements.
# after the alteration of code, it passes the the test.
# this is how unit test plays important role in finding the bug in the code.
# and improve the code so that it satisfy any input entered.
    
