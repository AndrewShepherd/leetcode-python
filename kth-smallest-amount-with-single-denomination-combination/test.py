import unittest
from kth_smallest_amount_with_single_denomination_combination import Solution

class TestSolution(unittest.TestCase):


    def test_0(self):
        coins = [6,15,16,20,22]
        """
        1: 6
        2: 12
        3: 15
        4: 16
        5: 18
        6: 20
        7: 22
        8: 24
        9: 30    # 6, 15
        10: 32
        11: 36
        12: 40
        13: 42
        14: 44
        15: 45
        16: 48 # 6, 16
        17: 54 # 6
        18: 60  # 6, 15, 20
        19: 64  # 16
        20: 66  # 6, 22
        """
        k = 25727
        s = Solution()
       # self.assertEqual(54, s.findKthSmallest(coins, 17))
       # self.assertEqual(60, s.findKthSmallest(coins, 18))
        self.assertEqual(64, s.findKthSmallest(coins, 19))
        self.assertEqual(88434, s.findKthSmallest(coins, k))


    def test_1(self):
        coins = [10,3,7,5]
        k = 7
        s = Solution()
        self.assertEqual(12, s.findKthSmallest(coins, k))

    def test_4(self):
        coins = [6,1,2,4]
        k = 4
        s = Solution()
        self.assertEqual(4, s.findKthSmallest(coins, k))

    def test_3(self):
        coins = [3,6,9]
        k = 3
        s = Solution()
        self.assertEqual(9, s.findKthSmallest(coins, k))

    def test_2(self):
        coins = [5,2]
        k = 7
        s = Solution()
        self.assertEqual(12, s.findKthSmallest(coins, k))

    def test_5(self):
        coins = [16,17,18,19,20,21,22,23,24,25]
        k = 2000000000
        s = Solution()
        result = s.findKthSmallest(coins, k)
       # self.assertEqual(None, s.findKthSmallest(coins, k))

try:
    unittest.main()
except SystemExit:
    None










