import unittest

from sum_of_digit_differences_of_all_pairs import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        sol = Solution()
        nums = [50,28,48]
        expected_result = 5
        result = sol.sumDigitDifferences(nums)
        self.assertEqual(expected_result, result)

    def test_1(self):
        sol = Solution()
        nums = [13,23,12]
        expected_result = 4
        result = sol.sumDigitDifferences(nums)
        self.assertEqual(expected_result, result)

    def test_2(self):
        sol = Solution()
        nums = [10,10,10]
        expected_result = 0
        result = sol.sumDigitDifferences(nums)
        self.assertEqual(expected_result, result)

try:
    unittest.main()
except SystemExit:
    None


