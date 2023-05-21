import unittest

from maximum_number_of_moves_in_a_grid import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
        result = s.maxMoves(grid)
        self.assertEqual(3, result)

    def test_2(self):
        s = Solution()
        grid = [[3,2,4],[2,1,9],[1,1,7]]
        result = s.maxMoves(grid)
        self.assertEqual(0, result)

try:
    unittest.main()
except SystemExit:
    None

