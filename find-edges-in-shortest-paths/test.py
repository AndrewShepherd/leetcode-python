import unittest

from find_edges_in_shortest_paths import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        n = 6
        edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]
        result = sol.findAnswer(n, edges)
        expected_result = [True,True,True,False,True,True,True,False]
        self.assertEqual(expected_result, result)

    def test_2(self):
        sol = Solution()
        n = 4
        edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]
        result = sol.findAnswer(n, edges)
        expected_result = [True,False, False, True]
        self.assertEqual(expected_result, result)

    def test_0(self):
        sol = Solution()
        n = 3
        edges = [[2,1,6]]
        result = sol.findAnswer(n, edges)
        expected_result = [True,False, False, True]
        self.assertEqual(expected_result, result)

try:
    unittest.main()
except SystemExit:
    None


















