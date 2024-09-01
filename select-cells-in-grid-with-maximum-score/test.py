import unittest

from select_cells_in_grid_with_maximum_score import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        grid = [1,2,3],[4,3,2],[1,1,1]
        result = sol.maxScore(grid)
        self.assertEqual(8, result)

    def test_2(self):
        sol = Solution()
        grid = [[8,7,6],[8,3,2]]
        result = sol.maxScore(grid)
        self.assertEqual(15, result)

    def test_0(self):
        sol = Solution()
        grid = [
            list(range(1, 11))
            for _ in range(10)
        ]
        result = sol.maxScore(grid)
        self.assertEqual(None, result)        


try:
    unittest.main()
except SystemExit:
    None



















