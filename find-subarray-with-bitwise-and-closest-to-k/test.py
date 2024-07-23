import unittest

from find_subarray_with_bitwise_and_closest_to_k import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        nums = [1,2,4,5]
        k = 3
        expected_result = 1
        result = sol.minimumDifference(nums, k)
        self.assertEqual(expected_result, result)

    def test_2(self):
        sol = Solution()
        nums = [1,2,1,2]
        k = 2
        expected_result = 0
        result = sol.minimumDifference(nums, k)
        self.assertEqual(expected_result, result)


try:
    unittest.main()
except SystemExit:
    None




