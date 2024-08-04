import unittest

from shortest_distance_after_road_addition_queries_i import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        n = 5
        queries = [[2,4],[0,2],[0,4]]
        sol = Solution()
        output = sol.shortestDistanceAfterQueries(n, queries)
        self.assertEqual(output, [3,2,1])

    def test_2(self):
        n = 4
        queries = [[0,3],[0,2]]
        sol = Solution()
        output = sol.shortestDistanceAfterQueries(n, queries)
        self.assertEqual(output, [1,1])






try:
    unittest.main()
except SystemExit:
    None

















