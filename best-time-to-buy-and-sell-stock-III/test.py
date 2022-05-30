import unittest


from best_time_to_buy_and_sell_stock_III import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, prices, expectedResult):
        sol= Solution()
        result = sol.maxProfit(prices)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [2,1,2,0,1],
            2
        )

    def test_4(self):
        self.run_test(
            [3,3,5,0,0,3,1,4],
            6
        )

    def test_2(self):
        self.run_test(
            [1,2,3,4,5],
            4
        )

    def test_3(self):
        self.run_test(
            [7,6,4,3,1],
            0
        )

try:
    unittest.main()
except SystemExit:
    None
