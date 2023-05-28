import unittest

from make_smallest_palindrome import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        input = "abcd"
        result = s.makeSmallestPalindrome(input)
        self.assertEqual('abba', result)

    def test_1(self):
        s = Solution()
        input = "seven"
        result = s.makeSmallestPalindrome(input)
        self.assertEqual('neven', result)

try:
    unittest.main()
except SystemExit:
    None




