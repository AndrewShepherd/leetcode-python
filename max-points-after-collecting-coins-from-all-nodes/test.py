import unittest

from max_points_after_collecting_coins_from_all_nodes import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()
        edges = [[0,1],[1,2],[2,3]]
        coins = [10,10,3,3]
        k = 5
        result = s.maximumPoints(edges, coins, k)
        self.assertEqual(11, result)

    def test_2(self):
        s = Solution()
        edges = [[0,1],[0,2]]
        coins = [8,4,4]
        k = 0
        result = s.maximumPoints(edges, coins, k)
        self.assertEqual(16, result)

    def test_1(self):
        s = Solution()
        edges = [[0,1],[2,0],[0,3],[4,2]]
        coins = [7,5,0,9,3]
        k = 4
        #
        # (0, 1)
        #  |
        #  +-- (2, 0)
        #  |     |
        #  |     +--- (4, 3)
        #  |
        #  +-- (3, 9)


        result = s.maximumPoints(edges, coins, k)
        self.assertEqual(10, result)

try:
    unittest.main()
except SystemExit:
    None












