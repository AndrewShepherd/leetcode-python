import unittest
from maximize_score_of_numbers_in_ranges import Solution

class TestSolution(unittest.TestCase):

    def test_001(self):
        start = [2,2,100]
        d = 5
        sol = Solution()
        output = sol.maxPossibleScore(start, d)
        self.assertEqual(output, 5)

    def test_002(self):
        start = [2,6,13,13]
        d = 5
        sol = Solution()
        output = sol.maxPossibleScore(start, d)
        self.assertEqual(output, 5)

    def test_003(self):
        start = [6,0,3]
        d = 2
        sol = Solution()
        output = sol.maxPossibleScore(start, d)
        self.assertEqual(output, 4) 









try:
    unittest.main()
except SystemExit:
    None

















