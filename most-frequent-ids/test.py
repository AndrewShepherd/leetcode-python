import unittest

from most_frequent_ids import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        nums = [2,3,2,1]
        freq = [3,2,-3,1]
        output = [3,3,2,2]
        result = sol.mostFrequentIDs(nums, freq)
        self.assertEqual(output, result)

    def test_2(self):
        sol = Solution()
        nums = [5,5,3]
        freq = [2,-2,1]
        output = [2,0,1]
        result = sol.mostFrequentIDs(nums, freq)
        self.assertEqual(output, result)


try:
    unittest.main()
except SystemExit:
    None













