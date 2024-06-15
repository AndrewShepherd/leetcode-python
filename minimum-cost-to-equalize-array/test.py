import unittest

from min_cost_to_equalize_array import Solution, tricky_calculation


class TestSolution(unittest.TestCase):


    def test_00(self):
        sol = Solution()
        nums = [47,14,36,99,128,200,151,132,151,180,13,38,135,2,140,78,58,109,53,39,149,133,163,42,154,139,89,5,81,143,109,183,62]
        cost1 = 23
        cost2 = 20
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(33463, result) 

    def test_15(self):
        sol = Solution()
        nums = [72678,82695,281,29915]
        cost1 = 858
        cost2 = 456
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(42053634, result) 

    def test_14(self):
        sol = Solution()
        nums = [1,1000000]
        cost1 = 1000000
        cost2 = 2
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(998993007, result) 

    def test_13(self):
        sol = Solution()
        nums = [1,1,1,1,1,1]
        cost1 = 1000000
        cost2 = 1000000
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(0, result)   


    def test_12(self):
        sol = Solution()
        nums = [69,19,66,69]
        cost1 = 80
        cost2 = 1
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(152, result)   

    def test_11(self):
        sol = Solution()
        nums = [55,52,29,11]
        cost1 = 18
        cost2 = 2
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(118, result)        

    def test_10(self):
        sol = Solution()
        nums = [5,5,7,8]
        cost1 = 7
        cost2 = 5
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(22, result) 

        

    def test_9(self):
        sol = Solution()
        nums = [4,3,1,8]
        cost1 = 5
        cost2 = 1
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(8, result) 

    def test_8(self):
        sol = Solution()
        nums = [10,9,45]
        cost1 = 31
        cost2 = 8
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(296, result)

    def test_7(self):
        sol = Solution()
        nums = [44,17,2]
        cost1 = 10
        cost2 = 7
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(339, result)

    def test_6(self):
        sol = Solution()
        nums = [3,9,1]
        cost1 = 5
        cost2 = 7
        result = sol.minCostToEqualizeArray(nums, cost1, cost2)
        self.assertEqual(52, result)

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

    def test_5(self):
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

    # [3] and [0]: nums = [2,14,15,15], cost = 1
    # [2] and [0]: nums = [3,15,15,15], cost = 2
    # Three Moves  nums = [6,16,16,16], cost = 5
    # Fifteen Moves nums = [21,21,21,21] cost = 20

    def test_2(self):
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
