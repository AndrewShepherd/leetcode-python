import unittest

from string_transformation import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        s = "a"
        t = "a"
        k = 1
        result = solution.numberOfWays(s, t, k)
        self.assertEqual(1, result)

    def test_2(self):
        solution = Solution()
        s = "abc"
        t = "abc"
        k = 1
        result = solution.numberOfWays(s, t, k)
        self.assertEqual(0, result)

    def test_3(self):
        solution = Solution()
        s = "abc"
        t = "cba"
        k = 3
        result = solution.numberOfWays(s, t, k)
        self.assertEqual(0, result)

    def test_5(self):
        solution = Solution()
        s = "abcd"
        t = "cdab"
        k = 2
        result = solution.numberOfWays(s, t, k)
        self.assertEqual(2, result)

    def test_6(self):
        solution = Solution()
        s = "ababab"
        t = "ababab"
        k = 1
        result = solution.numberOfWays(s, t, k)
        self.assertEqual(2, result)


try:
    unittest.main()
except SystemExit:
    None








