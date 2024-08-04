import unittest

from count_substrings import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = "00011"
        sol = Solution()
        output = sol.numberOfSubstrings(s)
        self.assertEqual(output, 5)

    def test_2(self):
        s = "101101"
        sol = Solution()
        output = sol.numberOfSubstrings(s)
        self.assertEqual(output, 16) 






try:
    unittest.main()
except SystemExit:
    None
















