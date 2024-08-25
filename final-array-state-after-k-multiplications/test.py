import unittest

from final_array_state import Solution

class TestSolution(unittest.TestCase):

    def test_00(self):
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






















