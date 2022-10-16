import unittest

from count_subarrays_with_fixed_bounds import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, nums, minK: int, maxK: int, expected_result : bool):
        sol= Solution()
        result = sol.countSubarrays(nums, minK, maxK)
        self.assertEqual(result, expected_result)


    def test_1(self):
        self.run_test([1,3,5,2,7,5], 1, 5, 2)

    def test_2(self):
        self.run_test(nums = [1,1,1,1], minK = 1, maxK = 1, expected_result=10)

    def test_0(self):
        self.run_test(
            [35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913],
            35054,
            945315,
            81
        )



try:
    unittest.main()
except SystemExit:
    None










