import unittest


from is_power_of_two import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, n, expectedResult):
        sol= Solution()
        result = sol.isPowerOfTwo(n)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            1,
            True
        )

    def test_2(self):
        self.run_test(
            -16,
            False
        )

try:
    unittest.main()
except SystemExit:
    None
