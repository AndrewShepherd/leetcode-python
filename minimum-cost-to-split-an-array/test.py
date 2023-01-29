import unittest
from minimum_cost_to_split_an_array import Solution
import big_input



class TestSolution(unittest.TestCase):

    def test_00(self):
        nums = [0]
        k = 2
        expected = 2
        s = Solution()
        generated = s.minCost(nums, k)
        self.assertEqual(generated, expected)

    def test_01(self):
        nums = [0, 0]
        k = 3
        expected = 5   # [0,0]=2 + 3
        s = Solution()
        generated = s.minCost(nums, k)
        self.assertEqual(generated, expected)

    def test_12(self):
        nums = [1,2,1,2,1,3,3]
        k = 2
        expected = 8
        s = Solution()
        generated = s.minCost(nums, k)
        self.assertEqual(generated, expected)

    def test_11(self):
        nums = [1,2,1,2,1]
        k = 2
        expected = 6
        s = Solution()
        generated = s.minCost(nums, k)
        self.assertEqual(generated, expected)

    def test_10(self):
        nums = [1,2,1,2,1]
        k = 5
        expected = 10
        s = Solution()
        generated = s.minCost(nums, k)
        self.assertEqual(generated, expected)

    def test_13(self):
        nums = big_input.nums
        k = 10
        expected = 431
        s = Solution()
        generated = s.minCost(nums, k)
        self.assertEqual(generated, expected)

    def test_14(self):
        nums = big_input.nums2
        k = 552
        expected = 1552
        s = Solution()
        generated = s.minCost(nums, k)
        self.assertEqual(generated, expected)

try:
    unittest.main()
except SystemExit:
    None









