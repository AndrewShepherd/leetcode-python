import unittest


from string_to_integer import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, s, expectedResult):
        sol= Solution()
        result = sol.myAtoi(s)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            "42",
            42
        )

    def test_2(self):
        self.run_test(
            "-42",
            -42
        )

    def test_3(self):
        self.run_test(
            "4193 with words",
            4193
        )

    def test_4(self):
        self.run_test(
            "words and 987",
            0
        )

    def test_5(self):
        self.run_test(
            "-91283472332",
            -2147483648
        )


try:
    unittest.main()
except SystemExit:
    None
