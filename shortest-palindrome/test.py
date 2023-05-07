import unittest
import big_input
from shortest_palindrome import Solution


class TestSolution(unittest.TestCase):

    def test_3(self):
        st = "aacecaaa"
        s = Solution()
        result = s.shortestPalindrome(st)
        self.assertEqual("aaacecaaa", result)

    def test_1(self):
        st = "abcd"
        s = Solution()
        result = s.shortestPalindrome(st)
        self.assertEqual("dcbabcd", result)

    def test_2(self):
        st = big_input.st
        s = Solution()
        result = s.shortestPalindrome(st)


try:
    unittest.main()
except SystemExit:
    None

















