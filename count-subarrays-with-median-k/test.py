import unittest
from count_subarrays_with_median_k import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.countSubarrays(nums = [3,2,1,4,5], k = 4)
        self.assertEqual(3, result)

    def test_2(self):
        s = Solution()
        result = s.countSubarrays(nums = [2,3,1], k = 3)
        self.assertEqual(1, result)

try:
    unittest.main()
except SystemExit:
    None


