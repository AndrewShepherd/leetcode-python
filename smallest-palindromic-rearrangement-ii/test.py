from smallest_palindromic_rearrangement_ii import Solution
from big_input import big_input
import unittest

class TestSolution(unittest.TestCase):

    def test_01(self):
        s = "nyggyn"
        k = 4
        expectedResult = "nyggyn"
        sol = Solution()
        #1: gnyyng
        #2: gynnyg
        #3: ngyygn
        #4: nyggyn
        self.assertEqual("gnyyng", sol.smallestPalindrome(s, 1))
        self.assertEqual("gynnyg", sol.smallestPalindrome(s, 2))
        self.assertEqual("ngyygn", sol.smallestPalindrome(s, 3))
        self.assertEqual("nyggyn", sol.smallestPalindrome(s, 4))

        result = sol.smallestPalindrome(s, k)
        self.assertEqual(expectedResult, result)

    def test_04(self):
        s = big_input
        k = 764367
        sol = Solution()
        result = sol.smallestPalindrome(s, k)
        self.assertEqual(len(result), len(big_input))

    def test_05(self):
        s = "abba"
        k = 2
        expectedResult = "baab"
        sol = Solution()
        result = sol.smallestPalindrome(s, k)
        self.assertEqual(expectedResult, result)

    def test_02(self):
        s = "aa"
        k = 2
        expectedResult = ""
        sol = Solution()
        result = sol.smallestPalindrome(s, k)
        self.assertEqual(expectedResult, result)

    def test_03(self):
        s = "bacab"
        k = 1
        expectedResult = "abcba"
        sol = Solution()
        result = sol.smallestPalindrome(s, k)
        self.assertEqual(expectedResult, result)


try:
    unittest.main()
except SystemExit:
    None












