import unittest
import big_input

from minimum_cost_to_make_array_equal import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, nums, cost, expected_result):
        sol= Solution()
        result = sol.minCost(nums, cost)
        self.assertEqual(result, expected_result)

    def test_3(self):
        self.run_test(nums = big_input.nums, cost = big_input.cost, expected_result=1094938531763074)

    def test_1(self):
        self.run_test(nums = [1,3,5,2], cost = [2,3,1,14], expected_result=8)

    def test_2(self):
        self.run_test(nums = [2,2,2,2,2], cost = [4,2,8,1,3], expected_result=0)

try:
    unittest.main()
except SystemExit:
    None











