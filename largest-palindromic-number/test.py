import unittest


from largest_palindromic_number import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        result = s.largestPalindromic("444947137")
        self.assertEqual("7449447", result)

    def test_5(self):
        s = Solution()
        result = s.largestPalindromic("00009")
        self.assertEqual("9", result)

    def test_2(self):
        s = Solution()
        result = s.largestPalindromic("1100")
        self.assertEqual("1001", result)

try:
    unittest.main()
except SystemExit:
    None
