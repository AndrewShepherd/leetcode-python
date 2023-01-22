import unittest
from get_arrow_shots import Solution



class TestSolution(unittest.TestCase):

    def test_0(self):
        points = [[1,2],[3,4],[5,6],[7,8]]
        self.assertEqual(4, Solution().findMinArrowShots(points))

try:
    unittest.main()
except SystemExit:
    None





