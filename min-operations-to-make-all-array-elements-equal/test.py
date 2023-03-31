import unittest
from min_operations import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [3,1,6,8]
        queries = [1,5]
        output = [14, 10]
        s = Solution()
        self.assertEqual(output, s.minOperations(nums, queries))

    def test_2(self):
        nums = [2,9,6,3]
        queries = [10]
        output = [20]
        s = Solution()
        self.assertEqual(output, s.minOperations(nums, queries))




try:
    unittest.main()
except SystemExit:
    None











