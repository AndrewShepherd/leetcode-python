import unittest

from divide_two_integers import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, dividend, divisor, expectedResult):
        sol = Solution()
        result = sol.divide(dividend, divisor)
        self.assertEqual(result, expectedResult)

    def test_2(self):
        self.run_test(10, 3, 3)

    def test_3(self):
        self.run_test(7, -3, -2)

    def test_1(self):
        self.run_test(-2147483648, -1, 2147483647)

try:
    unittest.main()
except SystemExit:
    None