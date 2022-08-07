import unittest
from longest_ideal_subsequence import Solution




class TestSolution(unittest.TestCase):


    def test_0(self):
        s = Solution()
        result = s.longestIdealString("acfgbd", 2)
        self.assertEqual(4, result)

    def test_1(self):
        s = Solution()
        result = s.longestIdealString("abcd", 3)
        self.assertEqual(4, result)

 

try:
    unittest.main()
except SystemExit:
    None