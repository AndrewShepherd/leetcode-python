import unittest
from number_of_subarrays_with_lcm_equal_to_k import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        result = s.subarrayLCM([3,6,2,7,1], 6)
        self.assertEqual(4, result)

    def test_2(self):
        s = Solution()
        result = s.subarrayLCM([3], 2)
        self.assertEqual(0, result)
try:
    unittest.main()
except SystemExit:
    None






