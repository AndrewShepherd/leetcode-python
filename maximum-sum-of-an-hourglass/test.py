import unittest


from maximum_sum_of_an_hourglass import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, grid, expectedResult):
        sol= Solution()
        result = sol.maxSum(grid)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]],
            30
        )

    def test_2(self):
        self.run_test(
            [[1,2,3],[4,5,6],[7,8,9]],
            35
        )


try:
    unittest.main()
except SystemExit:
    None



