from minimum_total_distance import Solution
import big_input
import big_input2
import unittest

class TestSolution(unittest.TestCase):

    def test_3(self):
        s = Solution()
        result = s.minimumTotalDistance(robot = big_input.robot, factory = big_input.factory)
        self.assertEqual(1652544383, result)

    def test_0(self):
        s = Solution()
        result = s.minimumTotalDistance(robot = big_input2.robot, factory = big_input2.factory)
        self.assertEqual(672818294, result)

    def test_1(self):
        s = Solution()
        result = s.minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]])
        self.assertEqual(4, result)

    def test_2(self):
        s = Solution()
        result = s.minimumTotalDistance(robot = [1,-1], factory = [[-2,1],[2,1]])
        self.assertEqual(2, result)

    def test_4(self):
        s = Solution()
        result = s.minimumTotalDistance(robot = [9,11,99,101], factory = [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]])
        self.assertEqual(6, result) 

    def test_5(self):
        robot = [789300819,-600989788,529140594,-592135328,-840831288,209726656,-671200998]   
        factory = [[-865262624,6],[-717666169,0],[725929046,2],[449443632,3],[-912630111,0],[270903707,3],[-769206598,2],[-299780916,4],[-159433745,5],[-467185764,3],[849991650,7],[-292158515,6],[940410553,6],[258278787,0],[83034539,2],[54441577,3],[-235385712,2],[75791769,3]]
        s = Solution()
        result = s.minimumTotalDistance(robot, factory)
        self.assertEqual(582755368, result)   

try:
    unittest.main()
except SystemExit:
    None




