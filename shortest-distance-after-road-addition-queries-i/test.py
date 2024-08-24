import unittest
import big_test_case_1
import big_test_case_2

from shortest_distance_after_road_addition_queries_i import Solution

class TestSolution(unittest.TestCase):



    def test_6(self):
        n = 13
        queries = [[10,12],[3,5],[9,12]]
        sol = Solution()
        output = sol.shortestDistanceAfterQueries(n, queries)
        self.assertEqual(output, [11, 10, 9])

    def test_5(self):
        n = 12
        queries = [[4,7],[8,10],[0,7]]
        sol = Solution()
        output = sol.shortestDistanceAfterQueries(n, queries)
        self.assertEqual(output, [9,8,4])



    def test_4(self):
        n = 4
        queries = [[0, 2]]
        sol = Solution()
        output = sol.shortestDistanceAfterQueries(n, queries)
        self.assertEqual(output, [2])

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

    def test_3(self):
        n = big_test_case_1.n
        queries = big_test_case_1.queries
        sol = Solution()
        output = sol.shortestDistanceAfterQueries(n, queries)
        self.assertEqual(len(output), len(queries))

    def test_0(self):
        n = big_test_case_2.n
        queries = big_test_case_2.queries
        sol = Solution()
        output = sol.shortestDistanceAfterQueries(n, queries)
        self.assertEqual(len(output), len(queries))






try:
    unittest.main()
except SystemExit:
    None

















