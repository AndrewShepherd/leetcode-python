from find_weighted_median_node_in_tree import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 2
        edges = [[0,1,7]]
        queries = [[1,0],[0,1]]
        expected_result = [0,1]
        sol = Solution()
        result = sol.findMedian(n, edges, queries)
        self.assertEqual(expected_result, result)

    def test_2(self):
        n = 3
        edges = [[0,1,2],[2,0,4]]
        queries = [[0,1],[2,0],[1,2]]
        expected_result = [1,0,2]
        sol = Solution()
        result = sol.findMedian(n, edges, queries)
        self.assertEqual(expected_result, result)

    def test_3(self):
        n = 5
        edges = [[0,1,2],[0,2,5],[1,3,1],[2,4,3]]
        queries = [[3,4],[1,2]]
        expected_result = [2,2]
        sol = Solution()
        result = sol.findMedian(n, edges, queries)
        self.assertEqual(expected_result, result)
try:
    unittest.main()
except SystemExit:
    None
