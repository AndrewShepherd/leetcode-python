import unittest

from separate_black_and_white_balls import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        sol = Solution()
        s = "101"
        result = sol.minimumSteps(s)
        self.assertEqual(1, result)

    def test_1(self):
        sol = Solution()
        s = "100"
        result = sol.minimumSteps(s)
        self.assertEqual(2, result)

    def test_2(self):
        sol = Solution()
        s = "0111"
        result = sol.minimumSteps(s)
        self.assertEqual(0, result)

try:
    unittest.main()
except SystemExit:
    None










