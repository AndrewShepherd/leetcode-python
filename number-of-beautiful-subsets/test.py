import unittest
from beautifulSubsets import Solution

class TestSolution(unittest.TestCase):

    def test_2(self):
        nums = [2,4,6]
        k = 2
        s = Solution()
        self.assertEqual(4, s.beautifulSubsets(nums, k))

    def test_1(self):
        nums = [1]
        k = 1
        s = Solution()
        self.assertEqual(1, s.beautifulSubsets(nums, k))

    def test_0(self):
        nums = list(range(1, 21))
        k = 7
        s = Solution()
        self.assertEqual(46874, s.beautifulSubsets(nums, k))





try:
    unittest.main()
except SystemExit:
    None











