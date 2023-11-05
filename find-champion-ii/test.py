import unittest

from find_champion_ii import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        n = 3
        edges = [[0,1],[1,2]]
        result = s.findChampion(n, edges)
        self.assertEqual(0, result)

    def test_2(self):
        s = Solution()
        n = 4
        edges = [[0,2],[1,3],[1,2]]
        result = s.findChampion(n, edges)
        self.assertEqual(-1, result)

try:
    unittest.main()
except SystemExit:
    None












