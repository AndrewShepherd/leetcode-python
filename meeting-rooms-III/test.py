import unittest
from meeting_rooms_III import Solution


class TestSolution(unittest.TestCase):


    def test_1(self):
        s = Solution()
        result = s.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]])
        self.assertEqual(0, result)

    def test_2(self):
        s = Solution()
        result = s.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]])
        self.assertEqual(1, result)

    def test_0(self):
        s = Solution()
        result = s.mostBooked(2, [[0,10],[1,5],[2,7],[3,4],[8,11],[9,12]])
        self.assertEqual(0, result)


try:
    unittest.main()
except SystemExit:
    None




