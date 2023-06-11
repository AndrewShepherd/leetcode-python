import unittest


from diff_of_distinct_values import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        grid = [[1,2,3],[3,1,5],[3,2,1]]
        expected_result = [[1,1,0],[1,0,1],[0,1,1]]
        result = s.differenceOfDistinctValues(grid)
        self.assertEqual(expected_result, result)

try:
    unittest.main()
except SystemExit:
    None







