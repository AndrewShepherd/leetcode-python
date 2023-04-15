import unittest
import big_input_1
from largest_color_value import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        colors = "abaca"
        edges = [[0,1],[0,2],[2,3],[3,4]]
        output = 3
        s = Solution()
        result = s.largestPathValue(colors, edges)
        self.assertEqual(output, result)

    # Just 10,000 d's in a straight line
    def test_2(self):
        colors = big_input_1.colors
        edges = big_input_1.edges
        output = 100000
        s = Solution()
        result = s.largestPathValue(colors, edges)
        self.assertEqual(output, result)

try:
    unittest.main()
except SystemExit:
    None












