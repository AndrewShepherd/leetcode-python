from total_cost import Solution

import unittest


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        result = s.totalCost([17,12,10,2,7,2,11,20,8], k = 3, candidates = 4)
        self.assertEqual(11, result)

    def test_2(self):
        s = Solution()
        result = s.totalCost(costs = [1,2,4,1], k = 3, candidates = 3)
        self.assertEqual(4, result)

    def test_3(self):
        s = Solution()
        result = s.totalCost(costs = [1,2,3,4], k= 4, candidates = 4)
        self.assertEqual(10, result)



try:
    unittest.main()
except SystemExit:
    None


