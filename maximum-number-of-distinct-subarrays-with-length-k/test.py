from maximum_subarray_sum import Solution

import unittest
import big_input

class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()
        result = s.maximumSubarraySum(big_input.nums, big_input.k)
        self.assertEqual(3750025000, result)

    def test_one(self):
        s = Solution()
        result = s.maximumSubarraySum([1,5,4,2,9,9,9], 3)
        self.assertEqual(15, result)

    def test_two(self):
        s = Solution()
        result = s.maximumSubarraySum(nums = [4,4,4], k = 3)
        self.assertEqual(0, result)

    def test_three(self):
        s = Solution()
        result = s.maximumSubarraySum(nums = [5,3,9,2,6], k = 1)
        self.assertEqual(9, result)

    def test_four(self):
        s = Solution()
        result = s.maximumSubarraySum(nums = [5,3,9,2,6], k = 2)
        self.assertEqual(12, result)

try:
    unittest.main()
except SystemExit:
    None

