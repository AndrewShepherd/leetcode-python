import unittest

from count_submatrices import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        grid = [[7,6,3],[6,6,1]]
        k = 18
        expected_result = 4
        self.assertEqual(expected_result, s.countSubmatrices(grid, k))

    def test_2(self):
        s = Solution()
        grid = [[7,2,9],[1,5,0],[2,6,6]]
        k = 20
        expected_result = 6
        self.assertEqual(expected_result, s.countSubmatrices(grid, k))

       

try:
    unittest.main()
except SystemExit:
    None










