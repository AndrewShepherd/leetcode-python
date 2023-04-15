import unittest
from find_the_longest_balanced_substring import Solution

class TestSolution(unittest.TestCase):

    def test_0(self):
        s = "01000111"
        output = 6
        sol = Solution()
        self.assertEqual(output, sol.findTheLongestBalancedSubstring(s))

    def test_1(self):
        s = "00111"
        output = 4
        sol = Solution()
        self.assertEqual(output, sol.findTheLongestBalancedSubstring(s))

    def test_2(self):
        s = "111"
        output = 0
        sol = Solution()
        self.assertEqual(output, sol.findTheLongestBalancedSubstring(s))





try:
    unittest.main()
except SystemExit:
    None













