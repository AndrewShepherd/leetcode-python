from minimum_positive_sum_array import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_01(self):
        nums = [3, -2, 1, 4]
        l = 2
        r = 3
        expectedResult = 1
        s = Solution()
        result = s.minimumSumSubarray(nums, l, r)
        self.assertEqual(expectedResult, result)



try:
    unittest.main()
except SystemExit:
    None










