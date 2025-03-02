from identify_the_largest_outlier_in_an_array import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_01(self):
        nums = [2,3,5,10]
        expectedResult = 10
        s = Solution()
        result = s.getLargestOutlier(nums)
        self.assertEqual(expectedResult, result)

    def test_02(self):
        nums = [-2,-1,-3,-6,4]
        expectedResult = 4
        s = Solution()
        result = s.getLargestOutlier(nums)
        self.assertEqual(expectedResult, result)

    def test_03(self):
        nums = [1,1,1,1,1,5,5]
        expectedResult = 5
        s = Solution()
        result = s.getLargestOutlier(nums)
        self.assertEqual(expectedResult, result)

try:
    unittest.main()
except SystemExit:
    None












