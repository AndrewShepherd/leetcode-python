import unittest
from maximal_rectangle import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
        self.assertEqual(6,result)


try:
    unittest.main()
except SystemExit:
    None
