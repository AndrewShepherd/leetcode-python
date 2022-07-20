from max_sum_of_pair_with_equal_sum_of_digits import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = Solution()
        result = s.maximumSum([18,43,36,13,7])
        self.assertEqual(54,result)

    def test_2(self):
        s = Solution()
        result = s.maximumSum([10,12,19,14])
        self.assertEqual(-1,result)

    def test_1(self):
        s = Solution()
        result = s.maximumSum([9, 9])
        self.assertEqual(18, result)

    def test_3(self):
        s = Solution()
        result = s.maximumSum([9])
        self.assertEqual(-1, result)


try:
    unittest.main()
except SystemExit:
    None