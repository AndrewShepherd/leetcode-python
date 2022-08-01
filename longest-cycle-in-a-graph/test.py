from longest_cycle_in_a_graph import Solution

import unittest

class TestSolution(unittest.TestCase):


    def test_1(self):
        s = Solution()
        result = s.longestCycle([3,3,4,2,3])
        self.assertEqual(3, result)

    def test_2(self):
        s = Solution()
        result = s.longestCycle([2,-1,3,1])
        self.assertEqual(-1,result)

    def test_3(self):
        s = Solution()
        result = s.longestCycle([-1,4,-1,2,0,4])
        self.assertEqual(-1, result)

try:
    unittest.main()
except SystemExit:
    None