import unittest

from min_ops_to_make_median_k import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        sol = Solution()
        nums = [98,52]
        k = 82
        output = 14
        result = sol.minOperationsToMakeMedianK(nums, k)
        self.assertEqual(output, result)

    def test_1(self):
        sol = Solution()
        nums = [2,5,6,8,5]
        k = 4
        output = 2
        result = sol.minOperationsToMakeMedianK(nums, k)
        self.assertEqual(output, result)

    def test_2(self):
        sol = Solution()
        nums = [2,5,6,8,5]
        k = 7
        output = 3
        result = sol.minOperationsToMakeMedianK(nums, k)
        self.assertEqual(output, result)

    def test_3(self):
        sol = Solution()
        nums = [1,2,3,4,5,6]
        k = 4
        output = 0 
        result = sol.minOperationsToMakeMedianK(nums, k)
        self.assertEqual(output, result)

try:
    unittest.main()
except SystemExit:
    None















