from find_closest_node_to_two_given_nodes import Solution

import unittest

class TestSolution(unittest.TestCase):


    def test_1(self):
        s = Solution()
        result = s.closestMeetingNode([2,2,3,-1], 0, 1)
        self.assertEqual(2, result)

    def test_2(self):
        s = Solution()
        result = s.closestMeetingNode([1,2,-1], 0, 2)
        self.assertEqual(2,result)

    def test_3(self):
        s = Solution()
        result = s.closestMeetingNode([1,2,0], 0, 1)
        self.assertEqual(1,result)

try:
    unittest.main()
except SystemExit:
    None