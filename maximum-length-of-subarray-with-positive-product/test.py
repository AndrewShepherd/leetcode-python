import unittest


from maximum_length_of_subarray_with_positive_product import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, s, expectedResult):
        sol= Solution()
        result = sol.getMaxLen(s)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [1,-2,-3,4],
            4
        )

    def test_2(self):
        self.run_test(
            [0,1,-2,-3,-4],
            3
        )

    def test_3(self):
        self.run_test(
            [-1,-2,-3,0,1],
            2
        )

try:
    unittest.main()
except SystemExit:
    None
