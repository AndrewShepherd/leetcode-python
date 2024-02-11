import unittest

from number_of_arrays_that_match_a_pattern import Solution


class TestSolution(unittest.TestCase):

    def test_2(self):
        sol = Solution()
        nums = [1,2,3,4,5,6]
        pattern = [1,1]
        result = sol.countMatchingSubarrays(nums, pattern)
        self.assertEqual(4, result)

    def test_1(self):
        sol = Solution()
        nums = [1,4,4,1,3,5,5,3]
        pattern = [1,0,-1]
        result = sol.countMatchingSubarrays(nums, pattern)
        self.assertEqual(2, result)


try:
    unittest.main()
except SystemExit:
    None

















