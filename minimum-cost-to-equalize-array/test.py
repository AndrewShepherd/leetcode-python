import unittest

from min_cost_to_equalize_array import Solution, tricky_calculation


class TestSolution(unittest.TestCase):

    def test_4(self):
        sol = Solution()
        nums = [6,8,8]
        cost1 = 2
        cost2 = 1
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(4, result)     


    def test_1(self):
        sol = Solution()
        nums = [4,1]
        cost1 = 5
        cost2 = 2
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(15, result)

    def test_2(self):
        sol = Solution()
        nums = [2,3,3,3,5]
        cost1 = 2
        cost2 = 1
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(6, result)

    def test_3(self):
        sol = Solution()
        nums = [3,5,3]
        cost1 = 1
        cost2 = 3
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(4, result)

    def test_0(self):
        sol = Solution()
        nums = [1,14,14,15]
        cost1 = 2
        cost2 = 1
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(20, result)     


  


try:
    unittest.main()
except SystemExit:
    None
