import unittest

from minimum_array_end import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        n = 3
        x = 4
        result = sol.minEnd(n, x)
        self.assertEqual(6, result)

    def test_2(self):
        sol = Solution()
        n = 2
        x = 7
        result = sol.minEnd(n, x)
        self.assertEqual(15, result)

    def test_0(self):
        sol = Solution()
        n = 3
        x = 1
        result = sol.minEnd(n, x)
        self.assertEqual(5, result)

try:
    unittest.main()
except SystemExit:
    None



















