import unittest


from longest_valid_parenthes import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, s, expectedResult):
        sol= Solution()
        result = sol.longestValidParentheses(s)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            "(()",
            2
        )

    def test_2(self):
        self.run_test(
            ")()())",
            4
        )

    def test_3(self):
        self.run_test(
            "",
            0
        )

    def test_4(self):
        self.run_test(
            "())",
            2
        )

    def test_5(self):
        self.run_test("()()", 4)

    def test_0(self):
        self.run_test("()(())", 6)


try:
    unittest.main()
except SystemExit:
    None
