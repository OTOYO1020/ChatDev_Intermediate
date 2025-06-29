'''
Unit tests for the Dango Level Finder module.
'''
import unittest
from dango_level_finder import DangoLevelFinder
class TestDangoLevelFinder(unittest.TestCase):
    '''
    Test cases for the DangoLevelFinder class.
    '''
    def setUp(self):
        '''
        Set up the DangoLevelFinder instance for testing.
        '''
        self.finder = DangoLevelFinder()
    def test_valid_cases(self):
        '''
        Test valid dango strings.
        '''
        self.assertEqual(self.finder.find_greatest_dango_level("---o---"), 1)
        self.assertEqual(self.finder.find_greatest_dango_level("----o----"), 2)
        self.assertEqual(self.finder.find_greatest_dango_level("----o---o----"), 2)
        self.assertEqual(self.finder.find_greatest_dango_level("----o---o---o----"), 2)
    def test_no_dango(self):
        '''
        Test cases with no valid dango strings.
        '''
        self.assertEqual(self.finder.find_greatest_dango_level("----"), -1)
        self.assertEqual(self.finder.find_greatest_dango_level("o---o"), -1)
        self.assertEqual(self.finder.find_greatest_dango_level(""), -1)
    def test_edge_cases(self):
        '''
        Test edge cases.
        '''
        self.assertEqual(self.finder.find_greatest_dango_level("-o-"), 1)
        self.assertEqual(self.finder.find_greatest_dango_level("-"), -1)
        self.assertEqual(self.finder.find_greatest_dango_level("o"), -1)
        self.assertEqual(self.finder.find_greatest_dango_level("o---o---o"), -1)
        self.assertEqual(self.finder.find_greatest_dango_level("----o---o---o---o----"), 2)  # Additional test case
if __name__ == "__main__":
    unittest.main()