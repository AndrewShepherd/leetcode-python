import unittest

from minimum_string import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        s = 'aaba*'
        expected_result = 'aab'
        result = sol.clearStars(s)
        self.assertEqual(expected_result, result)

    def test_0(self):
        sol = Solution()
        s = 'dk**'
        expected_result = ''
        result = sol.clearStars(s)
        self.assertEqual(expected_result, result)


try:
    unittest.main()
except SystemExit:
    None



