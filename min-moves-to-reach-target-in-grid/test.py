from min_moves_to_reach_target_in_grid import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_0(self):
        sx = 1
        sy = 1
        tx = 2
        ty = 2
        expected_result = -1
        sol = Solution()
        result = sol.minMoves(sx, sy, tx, ty)
        self.assertEqual(expected_result, result)

    def test_1(self):
        sx = 1
        sy = 2
        tx = 5
        ty = 4
        expected_result = 2

        sol = Solution()
        result = sol.minMoves(sx, sy, tx, ty)
        self.assertEqual(expected_result, result)

    def test_2(self):
        sx = 0
        sy = 1
        tx = 2
        ty = 3
        expected_result = 3

        sol = Solution()
        result = sol.minMoves(sx, sy, tx, ty)
        self.assertEqual(expected_result, result)

    def test_3(self):
        sx = 0
        sy = 1
        tx = 9
        ty = 6
        expected_result = -1

        sol = Solution()
        result = sol.minMoves(sx, sy, tx, ty)
        self.assertEqual(expected_result, result)

    def test_4(self):
        sx = 8399
        sy = 3573
        tx = 189452928
        ty = 125553808
        expected_result = 19

        sol = Solution()
        result = sol.minMoves(sx, sy, tx, ty)
        self.assertEqual(expected_result, result)

    def test_5(self):
        sx = 1417
        sy = 3245
        tx = 64118992
        ty = 59528160
        expected_result = 20

        sol = Solution()
        result = sol.minMoves(sx, sy, tx, ty)
        self.assertEqual(expected_result, result)

    def test_6(self):
        sx = 5
        sy = 9
        tx = 118096
        ty = 136902
        expected_result = 19

        sol = Solution()
        result = sol.minMoves(sx, sy, tx, ty)
        self.assertEqual(expected_result, result)

    def test_7(self):
        sx = 1
        sy = 0
        tx = 4480
        ty = 36448
        expected_result = 19

        sol = Solution()
        result = sol.minMoves(sx, sy, tx, ty)
        self.assertEqual(expected_result, result)



try:
    unittest.main()
except SystemExit:
    None





