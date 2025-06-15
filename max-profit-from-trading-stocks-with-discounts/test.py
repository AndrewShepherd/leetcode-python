from max_profit_from_trading_stocks_with_discounts import Solution

import unittest

class TestSolution(unittest.TestCase):

    def test_01(self):
        n = 2
        present = [1,2]
        future = [4,3] 
        hierarchy = [[1,2]]
        budget = 3
        expected_result = 5
        sol = Solution()
        result = sol.maxProfit(n, present, future, hierarchy, budget)
        self.assertEqual(expected_result, result)

    def test_02(self):
        n = 2
        present = [3,4]
        future = [5,8]
        hierarchy = [[1,2]]
        budget = 4
        expected_result = 4
        sol = Solution()
        result = sol.maxProfit(n, present, future, hierarchy, budget)
        self.assertEqual(expected_result, result)

    def test_03(self):
        n = 3
        present = [4,6,8]
        future = [7,9,11]
        hierarchy = [[1,2],[1,3]]
        budget = 10
        expected_result = 10
        sol = Solution()
        result = sol.maxProfit(n, present, future, hierarchy, budget)
        self.assertEqual(expected_result, result)

    def test_04(self):
        n = 2
        present = [33,13]
        future = [34,15]
        hierarchy = [[1,2]]
        budget = 20
        expected_result = 2
        sol = Solution()
        result = sol.maxProfit(n, present, future, hierarchy, budget)
        self.assertEqual(expected_result, result)

    def test_05(self):
        n = 2
        present = [1,36]
        future = [28,6]
        hierarchy = [[1,2]]
        budget = 118
        expected_result = 27
        sol = Solution()
        result = sol.maxProfit(n, present, future, hierarchy, budget)
        self.assertEqual(expected_result, result)


try:
    unittest.main()
except SystemExit:
    None













