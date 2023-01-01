import unittest
from possible_bipartition import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 10
        dislikes = [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]
        s = Solution()
        self.assertTrue(s.possibleBipartition(n, dislikes))

try:
    unittest.main()
except SystemExit:
    None
