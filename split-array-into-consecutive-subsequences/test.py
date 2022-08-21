import unittest
from split_array_into_consecutive_subsequences import Solution
from large_input import large_input


class TestSolution(unittest.TestCase):


    def test_2(self):
        s = Solution()
        result = s.isPossible([1,2,3,4,6,7,8,9,10,11])
        self.assertTrue(result)

    def test_1(self):
        s = Solution()
        result = s.isPossible(large_input)
        self.assertFalse(result)

    def test_0(self):
        s = Solution()
        result = s.isPossible([1,2,3,4,5,5,6,7])
        self.assertTrue(result)

try:
    unittest.main()
except SystemExit:
    None