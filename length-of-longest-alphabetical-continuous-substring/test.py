import unittest


from longest_continuous_substring import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, input, expectedResult):
        sol= Solution()
        result = sol.longestContinuousSubstring(input)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            "abacaba",
            2
        )

    def test_2(self):
        self.run_test(
            "abcde",
            5,
        )

    def test_3(self):
        self.run_test(
            "awy",
            1
        )

try:
    unittest.main()
except SystemExit:
    None

