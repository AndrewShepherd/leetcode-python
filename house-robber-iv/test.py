import unittest
from min_capability import Solution


class TestSolution(unittest.TestCase):

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


try:
    unittest.main()
except SystemExit:
    None


