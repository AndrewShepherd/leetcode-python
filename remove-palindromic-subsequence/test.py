import unittest

from remove_palindromic_subsequence import Solution


class TestSolution(unittest.TestCase):

    def run_test(self, s, exprectedResult):
        sol = Solution()
        result = sol.removePalindromeSub(s)
        self.assertEqual(result, exprectedResult)

    def test_1(self):
        self.run_test("abbaaaab", 2)

    def test_2(self):
        self.run_test("baabb", 2)

    def test_3(self):
        self.run_test("abb", 2)

    def test_4(self):
        self.run_test("ababa", 1)


try:
    unittest.main()
except SystemExit:
    None
