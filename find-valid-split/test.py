import unittest
from find_valid_split import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [4,7,8,15,3,5]
        s = Solution()
        self.assertEqual(2, s.findValidSplit(nums))

    def test_0(self):
        nums = [4,7,15,8,3,5]
        s = Solution()
        self.assertEqual(-1, s.findValidSplit(nums))

try:
    unittest.main()
except SystemExit:
    None







