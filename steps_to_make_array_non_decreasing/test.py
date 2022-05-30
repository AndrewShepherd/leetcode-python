import unittest

from steps_to_make_array_non_decreasing import Solution


class TestSolution(unittest.TestCase):

    def run_test(self, nums, exprectedResult):
        sol = Solution()
        result = sol.totalSteps(nums)
        self.assertEqual(result, exprectedResult)

    def test_2(self):
        self.run_test(
            [5,3,4,4,7,3,6,11,8,5,11],
            3
        )

    def test_3(self):
        self.run_test(
            [4,5,7,7,13], 
            0
        )

    def test_4(self):
        self.run_test(
            [7,14,4,14,13,2,6,13],
            3
        )

    def test_5(self):
        self.run_test(
            [10,1,2,3,4,5,6,1,2,3],
            6
        )

    def test_1(self):
        self.run_test(
            [5,14,15,2,11,5,13,15],
            3
        )


try:
    unittest.main()
except SystemExit:
    None
