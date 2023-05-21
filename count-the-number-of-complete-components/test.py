import unittest

from count_complete_components import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        n = 6
        edges = [[0,1],[0,2],[1,2],[3,4]]
        result = s.countCompleteComponents(n, edges)
        self.assertEqual(3, result)

    def test_0(self):
        s = Solution()
        n = 6
        edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
        result = s.countCompleteComponents(n, edges)
        self.assertEqual(1, result)

try:
    unittest.main()
except SystemExit:
    None


