from min_time_for_k_connected_components import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 2
        edges = [[0,1,3]]
        k = 2
        expected_result = 3

        sol = Solution()
        result = sol.minTime(n, edges, k)
        self.assertEqual(expected_result, result)


    def test_2(self):
        n = 3
        edges = [[0,1,2],[1,2,4]]
        k = 3
        expected_result = 4
        
        sol = Solution()
        result = sol.minTime(n, edges, k)
        self.assertEqual(expected_result, result)

    def test_3(self):
        n = 3
        edges = [[0,2,5]]
        k = 2
        expected_result = 0
        
        sol = Solution()
        result = sol.minTime(n, edges, k)
        self.assertEqual(expected_result, result)

try:
    unittest.main()
except SystemExit:
    None





