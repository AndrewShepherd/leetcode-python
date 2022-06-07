import unittest


from replace_elements_in_an_array import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, nums, operations, expectedResult):
        sol= Solution()
        result = sol.arrayChange(nums, operations)
        self.assertEqual(result, expectedResult)



    def test_1(self):
        self.run_test(
            [1,2], [[1,3],[2,1],[3,2]],
            [2,1],
        )

    def test_2(self):
        self.run_test(
            [1,2,4,6], [[1,3],[4,7],[6,1]],
            [3,2,7,1]
        )


try:
    unittest.main()
except SystemExit:
    None
