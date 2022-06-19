import unittest
from container_with_most_water import Solution
from large_dataset import large_dataset

class TestSolution(unittest.TestCase):

    def run_test(self, s, expectedResult):
        sol= Solution()
        result = sol.maxArea(s)
        self.assertEqual(result, expectedResult)

    def test_2(self):
        self.run_test(
            [1,8,6,2,5,4,8,3,7],
            49
        )

    def test_1(self):
        self.run_test(
            large_dataset,
            50000000
        )


try:
    unittest.main()
except SystemExit:
    None
