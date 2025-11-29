from find_max_balanced_xor_subarray_length import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [3,1,3,2,0]
        expected_result = 4
        sol = Solution()
        result = sol.maxBalancedSubarray(nums)
        self.assertEqual(expected_result, result)

    def test_2(self):
        nums = [3,2,8,5,4,14,9,15]
        expected_result = 8
        sol = Solution()
        result = sol.maxBalancedSubarray(nums)
        self.assertEqual(expected_result, result)


    def test_3(self):
        nums = [0]
        expected_result = 0
        sol = Solution()
        result = sol.maxBalancedSubarray(nums)
        self.assertEqual(expected_result, result)
 

try:
    unittest.main()
except SystemExit:
    None









