import unittest
import big_input
from max_balanced_subsequence_sum import Solution



class TestSolution(unittest.TestCase):



    def test_1(self):
        s = Solution()
        nums = [3,3,5,6]
        result = s.maxBalancedSubsequenceSum(nums)
        self.assertEqual(14, result)

    def test_2(self):
        s = Solution()
        nums = [5,-1,-3,8]
        result = s.maxBalancedSubsequenceSum(nums)
        self.assertEqual(13, result)

    def test_3(self):
        s = Solution()
        nums = [-2,-1]
        result = s.maxBalancedSubsequenceSum(nums)
        self.assertEqual(-1, result)

    def test_4(self):
        s = Solution()
        nums = big_input.nums
        result = s.maxBalancedSubsequenceSum(nums)
        self.assertEqual(99995000050000, result)

try:
    unittest.main()
except SystemExit:
    None













