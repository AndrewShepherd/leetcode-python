import unittest

from rearrange_characters_to_make_target_string import Solution


class TestSolution(unittest.TestCase):

    def run_test(self, s, t, exprectedResult):
        sol = Solution()
        result = sol.rearrangeCharacters(s, t)
        self.assertEqual(result, exprectedResult)

    def test_1(self):
        self.run_test("ilovecodingonleetcode", "code", 2)

    def test_4(self):
        self.run_test("acbca", "abc", 1)

    def test_5(self):
        self.run_test("abbaccaddaeea", "aaaaa", 1) 

try:
    unittest.main()
except SystemExit:
    None
