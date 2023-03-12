import unittest
from rearrange_array import Solution

class TestSolution(unittest.TestCase):

    def test_0(self):
        nums = [2,-1,0,1,-3,3,-3]
        s = Solution()
        self.assertEqual(6, s.maxScore(nums))

    def test_1(self):
        nums = [-2,-3,0]
        s = Solution()
        self.assertEqual(0, s.maxScore(nums))

try:
    unittest.main()
except SystemExit:
    None









