import unittest


from common_factors import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, i1, i2, expectedResult):
        sol= Solution()
        result = sol.commonFactors(i1, i2)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            12, 6,
            4
        )

    def test_2(self):
        self.run_test(
            25,30,
            2
        )


try:
    unittest.main()
except SystemExit:
    None


