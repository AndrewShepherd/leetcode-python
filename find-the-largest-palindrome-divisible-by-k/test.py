import unittest

from find_the_largest_palindrome import Solution

class TestSolution(unittest.TestCase):

    def test_0(self):
        n = 15
        k = 8
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, '888999999999888')

    def test_8(self):
        n = 2
        k = 2
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "88")

    def test_11(self):
        n = 16
        k = 7
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "9999999779999999")

    def test_12(self):
        n = 31
        k = 7
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "9999999999999994999999999999999")

    def test_13(self):
        n = 31
        k = 6
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "8999999999999998999999999999998")

    def test_10(self):
        n = 16
        k = 4
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "8899999999999988")

    def test_7(self):
        n = 1
        k = 1
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "9")

    def test_1(self):
        n = 3
        k = 5
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "595")

    def test_2(self):
        n = 1
        k = 4
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "8")

    def test_3(self):
        n = 5
        k = 6
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "89898")

    def test_9(self):
        n = 7
        k = 8
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "8889888")      

    def test_4(self):
        n = 5
        k = 5
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "59995")

    def test_5(self):
        n = 3
        k = 7
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, "959")

    def test_6(self):
        n = 11
        k = 8
        sol = Solution()
        output = sol.largestPalindrome(n, k)
        self.assertEqual(output, '88899999888')






try:
    unittest.main()
except SystemExit:
    None





















