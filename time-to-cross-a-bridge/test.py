import unittest
from find_crossing_time import Solution



class TestSolution(unittest.TestCase):


    def test_3(self):
        n = 10
        k = 6
        time = [[2,10,5,8],[3,5,2,2],[5,8,10,10],[7,8,8,5],[5,6,6,10],[6,10,6,2]]
        result = Solution().findCrossingTime(n, k, time)

    def test_1(self):
        n = 1
        k = 3
        time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
        self.assertEqual(6, Solution().findCrossingTime(n, k, time))

    def test_2(self):
        n = 3
        k = 2
        time = [[1,9,1,8],[10,10,10,10]]
        self.assertEqual(50, Solution().findCrossingTime(n, k, time))

    def test_0(self):
        n = 9
        k = 6
        time = [[2,6,9,4],[4,8,7,5],[4,6,7,6],[2,3,3,7],[9,3,6,8],[2,8,8,4]]
        s = Solution()
        result = s.findCrossingTime(n, k, time)
        self.assertEqual(115, result)


try:
    unittest.main()
except SystemExit:
    None






