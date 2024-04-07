import unittest

from smallest_string_after_ops_with_constraint import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        s = "zbbz"
        k = 3
        output = "aaaz"
        result = sol.getSmallestString(s, k)
        self.assertEqual(output, result)

    def test_2(self):
        sol = Solution()
        s = "xaxcd"
        k = 4
        output = "aawcd"
        result = sol.getSmallestString(s, k)
        self.assertEqual(output, result)

    def test_3(self):
        sol = Solution()
        s = "lol"
        k = 0
        output = "lol"
        result = sol.getSmallestString(s, k)
        self.assertEqual(output, result)


try:
    unittest.main()
except SystemExit:
    None














