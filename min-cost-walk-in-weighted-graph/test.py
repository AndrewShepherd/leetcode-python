import unittest

from min_cost_walk_in_weighted_graph import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        sol = Solution()
        n = 9
        edges = [[0,4,7],[3,5,1],[1,3,5],[1,5,1]]
        query = [[0,4],[1,5],[3,0],[3,3],[3,2],[2,0],[7,7],[7,0]]
        output = [7,1,-1,0,-1,-1,0,-1]
        result = sol.minimumCost(n, edges, query)
        self.assertEqual(output, result)

    def test_2(self):
        sol = Solution()
        n = 5
        edges = [[0,1,7],[1,3,7],[1,2,1]]
        query = [[0,3],[3,4]]
        output = [1,-1]
        result = sol.minimumCost(n, edges, query)
        self.assertEqual(output, result)

    def test_1(self):
        sol = Solution()
        n = 3
        edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
        query = [[1,2]]
        output = [0]
        result = sol.minimumCost(n, edges, query)
        self.assertEqual(output, result)

try:
    unittest.main()
except SystemExit:
    None
















