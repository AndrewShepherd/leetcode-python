import unittest
from sum_of_subarrays import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [1,2,-1,3,3,4]
        k = 2
        m = 2
        expected_result = 13
        sol = Solution()
        result =    sol.maxSum(nums, k, m)
        self.assertEqual(expected_result, result)

    def test_2(self):
        nums = [-10,3,-1,-2]
        k = 4
        m = 1
        expected_result = -10
        sol = Solution()
        result =    sol.maxSum(nums, k, m)
        self.assertEqual(expected_result, result)


try:
    unittest.main()
except SystemExit:
    None












