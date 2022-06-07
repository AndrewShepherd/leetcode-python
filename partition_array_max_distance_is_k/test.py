import unittest


from partition_array_max_distance_is_k import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, input, k, expectedResult):
        sol= Solution()
        result = sol.partitionArray(input, k)
        self.assertEqual(result, expectedResult)

    def test_3(self):
        self.run_test(
            [3,6,1,2,5], 2,
            2
        )

    def test_5(self):
        self.run_test(
            [1,2,3], 1,
            2,
        )

    def test_2(self):
        self.run_test(
            [2,2,4,5], 0,
            3,
        )

    def test_1(self):
        self.run_test(
            [3,1,3,4,2], 0,
            4
        )


try:
    unittest.main()
except SystemExit:
    None
