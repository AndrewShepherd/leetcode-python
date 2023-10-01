import unittest

from minimum_moves_to_spread_stones_over_grid import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        grid = [[1,1,0],[1,1,1],[1,2,1]]
        result = s.minimumMoves(grid)
        self.assertEqual(3, result)

    def test_2(self):
        s = Solution()
        grid = [[1,3,0],[1,0,0],[1,0,3]]
        result = s.minimumMoves(grid)
        self.assertEqual(4, result)

    def test_0(self):
        s = Solution()
        grid = [[3,2,0],[0,1,0],[0,3,0]]
        result = s.minimumMoves(grid)
        self.assertEqual(7, result)      

try:
    unittest.main()
except SystemExit:
    None







