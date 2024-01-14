import unittest

from max_number import Solution


class TestSolution(unittest.TestCase):



    def test_2(self):
        sol = Solution()
        k = 9
        x = 1
        result = sol.findMaximumNumber(k, x)
        self.assertEqual(6, result)

    def test_1(self):
        sol = Solution()
        k = 7
        x = 2
        result = sol.findMaximumNumber(k, x)
        self.assertEqual(9, result)

    def test_3(self):
        sol = Solution()
        k = 10**15
        x = 8
        result = sol.findMaximumNumber(k, x)
        self.assertEqual(None, result)

try:
    unittest.main()
except SystemExit:
    None















