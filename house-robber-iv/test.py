import unittest
from min_capability import Solution
import big_input


class TestSolution(unittest.TestCase):

    def test_0(self):
        nums = [1,2,3,4,5,6]
        k = 3
        s = Solution()
        result = s.minCapability(nums, k)
        self.assertEqual(5, result)

    def test_6(self):
        nums = [7,3,9,5]
        k = 2
        s = Solution()
        result = s.minCapability(nums, k)
        self.assertEqual(5, result)

    def test_3(self):
        nums = [4,22,11,14,25]
        k = 3
        s = Solution()
        result = s.minCapability(nums, k)
        self.assertEqual(25, result)

    def test_1(self):
        nums = [2,3,5,9]
        k = 2
        s = Solution()
        result = s.minCapability(nums, k)
        self.assertEqual(5, result)

    def test_2(self):
        nums = [2,7,9,3,1]
        k = 2
        s = Solution()
        result = s.minCapability(nums, k)
        self.assertEqual(2, result)

    def test_5(self):
        nums = big_input.nums
        k = big_input.k
        s = Solution()
        result = s.minCapability(nums, k)
        self.assertEqual(21499414, result)

try:
    unittest.main()
except SystemExit:
    None


