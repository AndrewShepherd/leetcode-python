import unittest
from maximum_multiplication_score import Solution

class TestSolution(unittest.TestCase):

    def test_001(self):
        a = [3,2,5,6]
        b = [2,-6,4,-5,-3,2,-7]
        sol = Solution()
        output = sol.maxScore(a, b)
        self.assertEqual(output, 26)

    def test_002(self):
        a = [-1,4,5,-2]
        b = [-5,-1,-3,-2,-4]
        sol = Solution()
        output = sol.maxScore(a, b)
        self.assertEqual(output, -1)










try:
    unittest.main()
except SystemExit:
    None


















