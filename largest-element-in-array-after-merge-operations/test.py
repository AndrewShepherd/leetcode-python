import unittest

from max_array_value import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        nums = [2,3,7,9,3]
        result = s.maxArrayValue(nums)
        self.assertEqual(21, result)


try:
    unittest.main()
except SystemExit:
    None



