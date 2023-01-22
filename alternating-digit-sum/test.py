import unittest
from alternating_digit_sum import Solution



class TestSolution(unittest.TestCase):

    def test_0(self):
        n = 521
        self.assertEqual(4, Solution().alternateDigitSum(n))

    def test_2(self):
        n = 886996
        self.assertEqual(0, Solution().alternateDigitSum(n))

    def test_3(self):
        n = 111
        self.assertEqual(1, Solution().alternateDigitSum(n))


try:
    unittest.main()
except SystemExit:
    None






