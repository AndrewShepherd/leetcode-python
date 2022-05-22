import unittest


from maximum_bags_with_full_capacity_of_rocks import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, capacity, rocks, additionalRocks, expectedResult):
        sol= Solution()
        result = sol.maximumBags(capacity, rocks, additionalRocks)
        self.assertEqual(result, expectedResult)

    def test_one(self):
        self.run_test([2,3,4,5], [1,2,4,4], 2, 3)

    def test_two(self):
        self.run_test([10,2,2], [2,2,0], 100, 3)

try:
    unittest.main()
except SystemExit:
    None
