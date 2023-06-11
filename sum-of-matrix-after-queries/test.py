import unittest


from sum_of_matrix_after_queries import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        n = 3
        queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
        result = s.matrixSumQueries(3, queries)
        self.assertEqual(23, result)

    def test_2(self):
        s = Solution()
        n = 3
        queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
        result = s.matrixSumQueries(n, queries)
        self.assertEqual(17, result)

try:
    unittest.main()
except SystemExit:
    None










