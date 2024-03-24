import unittest

from remove_invalid_parentheses import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        s = "()())()"
        result = sol.removeInvalidParentheses(s)
        self.assertEqual(set(result), {"(())()","()()()"})

    def test_2(self):
        sol = Solution()
        s = "(a)())()"
        result = sol.removeInvalidParentheses(s)
        self.assertEqual(set(result), {"(a())()","(a)()()"})

    def test_3(self):
        sol = Solution()
        s = ")()"
        result = sol.removeInvalidParentheses(s)
        self.assertEqual(set(result), {"()"})       

try:
    unittest.main()
except SystemExit:
    None











