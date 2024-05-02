import unittest

from find_the_median_of_the_uniqueness_array import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        sol = Solution()
        nums = [1,2,3]
        # (1,1,1,2,2,3)
        # We want index 2
        result = sol.medianOfUniquenessArray(nums)
        self.assertEqual(1, result)

    def test_2(self):
        sol = Solution()
        nums = [3,4,3,4,5]
        result = sol.medianOfUniquenessArray(nums)
        self.assertEqual(2, result)

    def test_3(self):
        sol = Solution()
        nums = [4,3,5,4]
        # 1,1,1,1,2,2,2,3,3,3
        # There are 4 with 1 or more
        # There are 7 with 2 or more
        result = sol.medianOfUniquenessArray(nums)
        self.assertEqual(2, result)

    def test_1(self):
        sol = Solution()
        nums = [91,64,76,18,61,55,46,93,65,99]
        result = sol.medianOfUniquenessArray(nums)
        self.assertEqual(4, result)

try:
    unittest.main()
except SystemExit:
    None




















