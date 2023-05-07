import unittest
from min_cost_of_path_with_special_roads import Solution

class TestSolution(unittest.TestCase):

    def test_0(self):
        start = [1,1]
        target = [4,5]
        specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
        s = Solution()
        result = s.minimumCost(start, target, specialRoads)
        self.assertEqual(5, result)

    def test_1(self):
        start = [3,2]
        target = [5,7]
        specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
        s = Solution()
        result = s.minimumCost(start, target, specialRoads)
        self.assertEqual(7, result)

try:
    unittest.main()
except SystemExit:
    None

















