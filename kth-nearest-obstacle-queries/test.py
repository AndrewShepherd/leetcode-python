import unittest

from kth_nearest_obstacle_queries import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        queries = [[1,2],[3,4],[2,3],[-3,0]]
        k = 2
        result = sol.resultsArray(queries, k)
        self.assertEqual([-1,7,5,3], result)

    def test_2(self):
        sol = Solution()
        queries = [[5,5],[4,4],[3,3]]
        k = 1
        result = sol.resultsArray(queries, k)
        self.assertEqual([10,8,6], result)


try:
    unittest.main()
except SystemExit:
    None


















