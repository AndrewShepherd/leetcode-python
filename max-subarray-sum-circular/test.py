import unittest


from max_subarray_sum_circular import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, s, expectedResult):
        sol= Solution()
        result = sol.maxSubarraySumCircular(s)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [-2,4,-5,4,-5,9,4],
            15
        )

    def test_2(self):
        self.run_test(
            [-3,-2,-3],
            -2
        )

try:
    unittest.main()
except SystemExit:
    None
