import unittest

from minimum_size_subarray_in_infinite_array import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        nums = [1,2,3]
        target = 5
        result = s.minSizeSubarray(nums, target)
        self.assertEqual(2, result)

    def test_2(self):
        s = Solution()
        nums = [1,1,1,2,3]
        target = 4
        result = s.minSizeSubarray(nums, target)
        self.assertEqual(2, result)

#  3  2  0
#  0  1  0
#  0  3  0

    def test_3(self):
        s = Solution()
        nums = [2,4,6,8]
        target = 3
        result = s.minSizeSubarray(nums, target)
        self.assertEqual(-1, result)      

    def test_0(self):
        s = Solution()
        nums = [1,2]
        target = 72
        result = s.minSizeSubarray(nums, target)
        self.assertEqual(48, result)  

try:
    unittest.main()
except SystemExit:
    None







