import unittest
from longest_palindrome import Solution

class TestSolution(unittest.TestCase):

    def test_2(self):
        s = "abced"
        k = 2
        sol = Solution()
        result =    sol.longestPalindromicSubsequence(s, k)
        self.assertEqual(3, result)

    def test_1(self):
        s = "aaazzz"
        k = 4
        sol = Solution()
        result =    sol.longestPalindromicSubsequence(s, k)
        self.assertEqual(6, result)

    def test_3(self):
        s = "vd"
        k = 10
        sol = Solution()
        result =    sol.longestPalindromicSubsequence(s, k)
        self.assertEqual(2, result)

try:
    unittest.main()
except SystemExit:
    None











