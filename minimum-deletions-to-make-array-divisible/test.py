from minimum_deletions_to_make_array_divisible import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.minOperations([2,3,2,4,3],[9,6,9,3,15])
        self.assertEqual(2,result)

    def test_2(self):
        s = Solution()
        result = s.minOperations([4,3,6], [8,2,6,10])
        self.assertEqual(-1,result)

try:
    unittest.main()
except SystemExit:
    None