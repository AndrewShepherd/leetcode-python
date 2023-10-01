import unittest

from count_visited_nodes import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        edges = [1,2,0,0]
        result = s.countVisitedNodes(edges)
        self.assertEqual([3,3,3,4], result)

    def test_2(self):
        s = Solution()
        edges = [1,2,3,4,0]
        result = s.countVisitedNodes(edges)
        self.assertEqual([5,5,5,5,5], result)

    def test_0(self):
        s = Solution()
        edges = [8,17,14,8,14,12,16,11,4,14,19,6,8,8,2,10,2,1,1,18]
        result = s.countVisitedNodes(edges)
        self.assertEqual([5, 2, 2, 5, 3, 6, 4, 6, 4, 3, 5, 5, 5, 5, 2, 6, 3, 2, 3, 4], result)

try:
    unittest.main()
except SystemExit:
    None








