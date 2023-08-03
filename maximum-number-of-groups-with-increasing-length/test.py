import unittest

from max_increasing_groups import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        usageLimits = [1,2,5]
        result = s.maxIncreasingGroups(usageLimits)
        self.assertEqual(3, result)

    def test_2(self):
        s = Solution()
        usageLimits = [2,1,2]
        result = s.maxIncreasingGroups(usageLimits)
        self.assertEqual(2, result)

    def test_3(self):
        s = Solution()
        usageLimits = [1,1]
        result = s.maxIncreasingGroups(usageLimits)
        self.assertEqual(1, result)

    def test_4(self):
        s = Solution()
        usageLimits = [2, 2, 2]
        result = s.maxIncreasingGroups(usageLimits)
        self.assertEqual(3, result)

    def test_5(self):
        s = Solution()
        usageLimits = [1, 1, 1]
        result = s.maxIncreasingGroups(usageLimits)
        self.assertEqual(2, result)

    def test_6(self):
        s = Solution()
        usageLimits = [4, 1, 1]
        result = s.maxIncreasingGroups(usageLimits)
        self.assertEqual(2, result)
try:
    unittest.main()
except SystemExit:
    None




