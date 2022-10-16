import unittest

from count_distinct_integers import Solution
from big_dataset import bds

class TestSolution(unittest.TestCase):

    def run_test(self, nums, expected_result):
        sol= Solution()
        result = sol.countDistinctIntegers(nums)
        self.assertEqual(result, expected_result)


    def test_1(self):
        self.run_test([1,13,10,12,31], 6)

    def test_2(self):
        self.run_test([2,2,2], 1)

    def test_3(self):
        self.run_test(bds, 11305)

try:
    unittest.main()
except SystemExit:
    None









