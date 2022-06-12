from minimum_path_cost_in_grid import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        grid = [[5,3],[4,0],[2,1]]
        moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
        result = s.minPathCost(grid, moveCost)
        self.assertEqual(17,result)

    def test_2(self):
        s = Solution()
        grid = [[5,1,2],[4,0,3]]
        moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]
        result = s.minPathCost(grid, moveCost)
        self.assertEqual(6,result)


try:
    unittest.main()
except SystemExit:
    None