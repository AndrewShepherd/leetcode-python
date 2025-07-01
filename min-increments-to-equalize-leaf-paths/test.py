from min_increments_to_equalize_leaf_paths import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 3
        edges = [[0,1],[0,2]]
        cost = [2,1,3]
        expected_result = 1
        sol = Solution()
        result = sol.minIncrease(n, edges, cost)
        self.assertEqual(expected_result, result)

    def test_2(self):
        n = 3
        edges = [[0,1],[1,2]]
        cost = [5,1,4]
        expected_result = 0
        sol = Solution()
        result = sol.minIncrease(n, edges, cost)
        self.assertEqual(expected_result, result)

    def test_3(self):
        n = 5
        edges = [[0,4],[0,1],[1,2],[1,3]]
        cost = [3,4,1,1,7]
        expected_result = 1
        sol = Solution()
        result = sol.minIncrease(n, edges, cost)
        self.assertEqual(expected_result, result)
try:
    unittest.main()
except SystemExit:
    None


