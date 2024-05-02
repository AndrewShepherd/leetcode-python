import unittest

from min_ops_to_satisfy_conditions import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        grid = [[1,0,2],[1,0,2]]
        result = sol.minimumOperations(grid)
        self.assertEqual(0, result)

    def test_2(self):
        sol = Solution()
        grid = [[1,1,1],[0,0,0]]
        result = sol.minimumOperations(grid)
        self.assertEqual(3, result)


    def test_3(self):
        sol = Solution()
        grid = [[1],[2],[3]]
        result = sol.minimumOperations(grid)
        self.assertEqual(2, result)

try:
    unittest.main()
except SystemExit:
    None

















