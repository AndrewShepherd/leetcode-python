import unittest
from min_deviation_in_array import Solution



class TestSolution(unittest.TestCase):

    def test_0(self):
        nums = [399,908,648,357,693,502,331,649,596,698]
        s = Solution()
        result = s.minimumDeviation(nums)
        self.assertEqual(315, result)

try:
    unittest.main()
except SystemExit:
    None



