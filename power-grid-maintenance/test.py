from power_grid_maintenance import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        c = 5
        connections = [[1,2],[2,3],[3,4],[4,5]]
        queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
        expected_result = [3,2,3]

        sol = Solution()
        result = sol.processQueries(c, connections, queries)
        self.assertEqual(expected_result, result)





try:
    unittest.main()
except SystemExit:
    None




