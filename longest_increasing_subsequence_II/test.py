import unittest
from large_test_case import large_array
import large_test_case_II
import large_test_case_III


from longest_increasing_subsequence_II import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, input, k, expectedResult):
        sol= Solution()
        result = sol.lengthOfLIS(input, k)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [4,2,1,4,3,4,5,8,15], 3,
            5
        )

    def test_2(self):
        self.run_test(
           [7,4,5,1,8,12,4,7],5,
            4,
        )

    def test_0(self):
        self.run_test(
            large_array, 1,
            100000
        )

    def test_3(self):
        self.run_test(
            [6,14,7,10,1,3,18,6,17], 20,
            4
        )

    def test_4(self):
        self.run_test(
            large_test_case_II.nums, large_test_case_II.k,
            613
        )

    def test_5(self):
        self.run_test(
            large_test_case_III.nums, 50000,
            50000
        )
try:
    unittest.main()
except SystemExit:
    None

