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

try:
    unittest.main()
except SystemExit:
    None








