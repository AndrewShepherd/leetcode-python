import unittest

from max_size_of_set_after_removals import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()
        nums1 = [1,10,6,5]
        nums2 = [3,7,10,10]
        result = s.maximumSetSize(nums1, nums2)
        self.assertEqual(4, result)

    def test_1(self):
        s = Solution()
        nums1 = [1,2,1,2]
        nums2 = [1,1,1,1]
        result = s.maximumSetSize(nums1, nums2)
        self.assertEqual(2, result)

    def test_2(self):
        s = Solution()
        nums1 = [1,2,3,4,5,6]
        nums2 = [2,3,2,3,2,3]
        result = s.maximumSetSize(nums1, nums2)
        self.assertEqual(5, result)

    def test_3(self):
        s = Solution()
        nums1 = [1,1,2,2,3,3]
        nums2 = [4,4,5,5,6,6]
        result = s.maximumSetSize(nums1, nums2)
        self.assertEqual(6, result)

try:
    unittest.main()
except SystemExit:
    None












