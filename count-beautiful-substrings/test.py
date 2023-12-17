import unittest

from count_beautiful_substrings import Solution
import big_input


class TestSolution(unittest.TestCase):

    def test_0(self):
        sol = Solution()
        s = "ihroyeeb"
        k = 5
        result = sol.beautifulSubstrings(s, k)
        self.assertEqual(0, result)

    def test_1(self):
        sol = Solution()
        s = "baeyh"
        k = 2
        result = sol.beautifulSubstrings(s, k)
        self.assertEqual(2, result)

    def test_2(self):
        sol = Solution()
        s = "abba"
        k = 1
        result = sol.beautifulSubstrings(s, k)
        self.assertEqual(3, result)

    def test_3(self):
        sol = Solution()
        s = "bcdf"
        k = 1
        result = sol.beautifulSubstrings(s, k)
        self.assertEqual(0, result)

    def test_4(self):
        sol = Solution()
        s = big_input.s
        k = 2
        result = sol.beautifulSubstrings(s, k)
        self.assertEqual(312487500, result) # Has not yet been confirmed

try:
    unittest.main()
except SystemExit:
    None












