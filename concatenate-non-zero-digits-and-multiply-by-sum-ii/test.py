from sum_and_multiply import Solution
import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = "10203004"
        queries = [[0,7],[1,3],[4,6]]
        expected_result = [12340, 4, 9]
        sol = Solution()
        result = sol.sumAndMultiply(s, queries)
        self.assertEqual(expected_result, result)

    def test_2(self):
        s = "1000"
        queries = [[0,3],[1,1]]
        expected_result = [1,0]
        sol = Solution()
        result = sol.sumAndMultiply(s, queries)
        self.assertEqual(expected_result, result)


    def test_3(self):
        s = "9876543210"
        queries = [[0,9]]
        expected_result = [444444137]
        sol = Solution()
        result = sol.sumAndMultiply(s, queries)
        self.assertEqual(expected_result, result)
 

try:
    unittest.main()
except SystemExit:
    None










