import unittest
from min_abs_diff_in_sliding_submatrix import Solution

class TestSolution(unittest.TestCase):

    def test_01(self):
        grid = [[1,8],[3,-2]]
        k = 2
        expectedResult = [[2]]
        sol = Solution()
        result = sol.minAbsDiff(grid, k)
        self.assertEqual(expectedResult, result)

    def test_02(self):
        grid = [[3,-1]]
        k = 1
        expectedResult = [[0,0]]
        sol = Solution()
        result = sol.minAbsDiff(grid, k)
        self.assertEqual(expectedResult, result)

    def test_03(self):
        grid = [[1,-2,3],[2,3,5]]
        k = 2
        expectedResult = [[1,2]]
        sol = Solution()
        result = sol.minAbsDiff(grid, k)
        self.assertEqual(expectedResult, result)

try:
    unittest.main()
except SystemExit:
    None













