from query_kth_smallest_trimmed_number import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.smallestTrimmedNumbers(["102","473","251","814"],[[1,1],[2,3],[4,2],[1,2]])
        self.assertEqual([2,2,1,0],result)

    def test_2(self):
        s = Solution()
        result = s.smallestTrimmedNumbers(["24","37","96","04"], [[2,1],[2,2]])
        self.assertEqual([3,0],result)

    def test_0(self):
        s = Solution()
        result = s.smallestTrimmedNumbers(["9415","5908","1840","5307"], [[3,2],[2,2],[3,3],[1,3]])
        self.assertEqual([0,1,2,3], result)

try:
    unittest.main()
except SystemExit:
    None