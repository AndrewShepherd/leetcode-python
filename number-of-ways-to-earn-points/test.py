import unittest
from number_of_ways_to_earn_points import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        target = 6
        types = [[6,1],[3,2],[2,3]]
        s = Solution()
        self.assertEqual(7, s.waysToReachTarget(target, types))

    def test_0(self):
        target = 5
        types = [[50,1],[50,2],[50,5]]
        s = Solution()
        self.assertEqual(4, s.waysToReachTarget(target, types))

    def test_2(self):
        target = 18
        types = [[6,1],[3,2],[2,3]]
        s = Solution()
        self.assertEqual(1, s.waysToReachTarget(target, types))

try:
    unittest.main()
except SystemExit:
    None








