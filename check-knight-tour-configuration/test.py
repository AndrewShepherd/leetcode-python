import unittest
from check_knight_tour_configuration import Solution

class TestSolution(unittest.TestCase):

    def test_2(self):
        grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
        s = Solution()
        self.assertEqual(True, s.checkValidGrid(grid))

    def test_1(self):
        grid = [[0,3,6],[5,8,1],[2,7,4]]
        s = Solution()
        self.assertEqual(False, s.checkValidGrid(grid))


    def test_0(self):
        grid = [[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]]
        s = Solution()
        self.assertEqual(False, s.checkValidGrid(grid))


try:
    unittest.main()
except SystemExit:
    None










