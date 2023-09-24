import unittest

from beautiful_towers_1 import Solution
import big_input


class TestSolution(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        maxHeights = [5,3,4,1,1]
        result = solution.maximumSumOfHeights(maxHeights)
        self.assertEqual(13, result)

    def test_2(self):
        solution = Solution()
        maxHeights = [6,5,3,9,2,7]
        result = solution.maximumSumOfHeights(maxHeights)
        self.assertEqual(22, result)

    def test_3(self):
        solution = Solution()
        maxHeights = [3,2,5,5,2,3]
        result = solution.maximumSumOfHeights(maxHeights)
        self.assertEqual(18, result)

    def test_4(self):
        solution = Solution()
        maxHeights = big_input.maxHeights
        result = solution.maximumSumOfHeights(maxHeights)
        self.assertEqual(3847648209262, result)

try:
    unittest.main()
except SystemExit:
    None










