from find_minimum_time_to_reach_last_room_I import Solution
import unittest

class TestSolution(unittest.TestCase):


    def test_1(self):
        moveTime = [[0,4],[4,4]]
        expectedResult = 6
        s = Solution()
        result = s.minTimeToReach(moveTime)
        self.assertEqual(expectedResult, result)

    def test_2(self):
        moveTime = [[0,0,0],[0,0,0]]
        expectedResult = 3
        s = Solution()
        result = s.minTimeToReach(moveTime)
        self.assertEqual(expectedResult, result)


try:
    unittest.main()
except SystemExit:
    None




