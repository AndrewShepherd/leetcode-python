import unittest

from max_operations import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        edges = [[0,1],[0,2],[0,3],[2,4],[4,5]]
        values = [5,2,5,2,1,1]
        result = s.maximumScoreAfterOperations(edges, values)
        self.assertEqual(11, result)

    def test_2(self):
        s = Solution()
        edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
        values = [20,10,9,7,4,3,5]
        result = s.maximumScoreAfterOperations(edges, values)
        self.assertEqual(40, result)

try:
    unittest.main()
except SystemExit:
    None













