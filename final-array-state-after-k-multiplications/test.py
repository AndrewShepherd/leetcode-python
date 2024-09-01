import unittest
import big_input
import math

from final_array_state import Solution

class TestSolution(unittest.TestCase):

    def test_00(self):
        nums = [9,81,729,6561,59049,531441,4782969,43046721,387420489]
        k = 1000000000
        multiplier = 9
        sol = Solution()
        output = sol.getFinalState(nums, k, multiplier)
        self.assertEqual(output, [994183796,332687090,332687090,332687090,332687090,332687090,332687090,332687090,332687090])

    def test_10(self):
        nums = big_input.nums
        k = big_input.k
        multiplier = big_input.m
        sol = Solution()
        output = sol.getFinalState(nums, k, multiplier)
        self.assertEqual(output, big_input.expected)

    def test_09(self):
        nums = [1,1000000000,1,1000000000]
        k = 4
        multiplier = 2
        sol = Solution()
        output = sol.getFinalState(nums, k, multiplier)
        self.assertEqual(output, [4,1000000000,4,1000000000])

    def test_08(self):
        nums = [5,1]
        k = 2
        multiplier = 3
        sol = Solution()
        output = sol.getFinalState(nums, k, multiplier)
        self.assertEqual(output, [5,9])

    def test_07(self):
        nums = [5,1,4,2]
        k = 4
        multiplier = 4
        sol = Solution()
        output = sol.getFinalState(nums, k, multiplier)
        self.assertEqual(output, [5,16,16,8])

    def test_06(self):
        nums = [2,4,5]
        k = 3
        multiplier = 4
        sol = Solution()
        output = sol.getFinalState(nums, k, multiplier)
        self.assertEqual(output, [8,16,20])

    def test_05(self):
        nums = [1]
        k = 1
        multiplier = 1
        sol = Solution()
        output = sol.getFinalState(nums, k, multiplier)
        self.assertEqual(output, [1])

    def test_04(self):
        nums = [2,1,3,5,6]
        k = 5
        multiplier = 2
        sol = Solution()
        output = sol.getFinalState(nums, k, multiplier)
        self.assertEqual(output, [8,4,6,5,6])

    def test_01(self):
        nums = [1,2]
        k = 3
        multiplier = 4
        sol = Solution()
        output = sol.getFinalState(nums, k, multiplier)
        self.assertEqual(output, [16,8])

    def test_02(self):
        nums = [100000,2000]
        k = 2
        multiplier = 1000000
        sol = Solution()
        output = sol.getFinalState(nums, k, multiplier)
        self.assertEqual(output, [999999307,999999993])

    def test_03(self):
        nums = [int(10**9)] * 1000
        k = int(10**9)
        multiplier = int(10**6)
        sol = Solution()
        output = sol.getFinalState(nums, k, multiplier) 






try:
    unittest.main()
except SystemExit:
    None






















