import unittest


from max_product_subarry import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, s, expectedResult):
        sol= Solution()
        result = sol.maxProduct(s)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [2,-5,-2,-4,3],
            24
        )

    def test_2(self):
        self.run_test(
            [2,3,-2, 4],
            6
        )

    def test_3(self):
        self.run_test(
            [0, 2, 0, 2, 0],
            2
        )

try:
    unittest.main()
except SystemExit:
    None
