import unittest

from max_palindromes_after_operations import Solution


class TestSolution(unittest.TestCase):




    def test_1(self):
        sol = Solution()
        words = ["abbb","ba","aa"]
        result = sol.maxPalindromesAfterOperations(words)
        self.assertEqual(3, result)

    def test_2(self):
        sol = Solution()
        words = ["abc","ab"]
        result = sol.maxPalindromesAfterOperations(words)
        self.assertEqual(2, result)

    def test_3(self):
        sol = Solution()
        words = ["cd","ef","a"]
        result = sol.maxPalindromesAfterOperations(words)
        self.assertEqual(1, result)

try:
    unittest.main()
except SystemExit:
    None
















