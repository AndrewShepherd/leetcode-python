import unittest

from apply_discount_to_prices import Solution


class TestSolution(unittest.TestCase):

    def run_test(self, sentence, discount, exprectedResult):
        sol = Solution()
        result = sol.discountPrices(sentence, discount)
        self.assertEqual(result, exprectedResult)

    def test_1(self):
        self.run_test(
            "there are $1 $2 and 5$ candies in the shop",
            50, 
            "there are $0.50 $1.00 and 5$ candies in the shop"
        )

    def test_2(self):
        self.run_test(
            "1 2 $3 4 $5 $6 7 8$ $9 $10$", 
            100,
            "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"
        )


try:
    unittest.main()
except SystemExit:
    None
