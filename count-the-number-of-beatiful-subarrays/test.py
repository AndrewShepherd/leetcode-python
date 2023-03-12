import unittest
import big_input
from count_beautiful_subarrays import Solution

class TestSolution(unittest.TestCase):

    def test_0(self):
        nums =  big_input.nums
        s = Solution()
        self.assertEqual(2, s.beautifulSubarrays(nums))

    def test_3(self):
        nums =  [4,3,1,2,4]
        s = Solution()
        self.assertEqual(2, s.beautifulSubarrays(nums))

    def test_1(self):
        nums =  [1,10,4]
        s = Solution()
        self.assertEqual(0, s.beautifulSubarrays(nums))

    def test_2(self):
        nums =  [0]
        s = Solution()
        self.assertEqual(1, s.beautifulSubarrays(nums))

try:
    unittest.main()
except SystemExit:
    None










