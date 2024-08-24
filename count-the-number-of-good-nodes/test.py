import unittest

from count_goodnodes import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
        sol = Solution()
        output = sol.countGoodNodes(edges)
        self.assertEqual(output, 7)

    def test_2(self):
        edges = [[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]]
        sol = Solution()
        output = sol.countGoodNodes(edges)
        self.assertEqual(output, 6)

    def test_3(self):
        edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
        sol = Solution()
        output = sol.countGoodNodes(edges)
        self.assertEqual(output, 7)



try:
    unittest.main()
except SystemExit:
    None


















