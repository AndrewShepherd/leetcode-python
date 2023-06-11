import unittest


from max_increasing_cells import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        mat = [[3,1],[3,4]]
        result = s.maxIncreasingCells(mat)
        self.assertEqual(2, result)

    def test_3(self):
        s = Solution()
        mat = [[1,1],[1,1]]
        result = s.maxIncreasingCells(mat)
        self.assertEqual(1, result)

    def test_2(self):
        s = Solution()
        mat = [[3,1,6],[-9,5,7]]
        result = s.maxIncreasingCells(mat)
        self.assertEqual(4, result)

try:
    unittest.main()
except SystemExit:
    None









