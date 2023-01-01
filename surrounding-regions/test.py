import unittest
from surrounding_regions import Solution


class TestSolution(unittest.TestCase):
    def test_2(self):
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        expected_result = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        s = Solution()
        s.solve(board)
        self.assertEqual(board, expected_result)

    def test_3(self):
        board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
        expected_result = [["X","O","X","X"],["O","X","X","X"],["X","X","X","O"],["O","X","O","X"]]
        s = Solution()
        s.solve(board)
        self.assertEqual(board, expected_result)

    def test_1(self):
        board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
        expected_result = [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
        s = Solution()
        s.solve(board)
        self.assertEqual(board, expected_result)

try:
    unittest.main()
except SystemExit:
    None

