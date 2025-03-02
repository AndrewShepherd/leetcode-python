import unittest
from patching_array import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [1,12,15]
        n = 43
        s = Solution()
        self.assertEqual(4, s.minPatches(nums, n))

    def test_4(self):
        nums = [1,5,10]
        n = 20
        s = Solution()
        self.assertEqual(2, s.minPatches(nums, n))

    def test_2(self):
        nums = [1,3]
        n = 6
        s = Solution()
        self.assertEqual(1, s.minPatches(nums, n))

    def test_3(self):
        nums = [1,2,2]
        n = 5
        s = Solution()
        self.assertEqual(0, s.minPatches(nums, n))

try:
    unittest.main()
except SystemExit:
    None










