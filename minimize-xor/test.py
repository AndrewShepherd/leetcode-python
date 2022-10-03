import unittest

from minimize_xor import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, num1, num2, expectedResult):
        sol= Solution()
        result = sol.minimizeXor(num1, num2)
        self.assertEqual(result, expectedResult)

    def test_0(self):
        self.run_test(
            65,84,
            67
        )

    def test_1(self):
        self.run_test(
            3,5,
            3
        )

    def test_2(self):
        self.run_test(
            1,12,
            3
        )


try:
    unittest.main()
except SystemExit:
    None




