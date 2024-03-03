import unittest

from largest_square_area import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()
        bottomLeft = [[2,2], [3,1]]
        topRight = [[5, 5], [5,5]]
        expected_result = 4
        self.assertEqual(expected_result, s.largestSquareArea(bottomLeft, topRight))

    def test_1(self):
        s = Solution()
        bottomLeft = [[1,1],[2,2],[3,1]]
        topRight = [[3,3],[4,4],[6,6]]
        expected_result = 1
        self.assertEqual(expected_result, s.largestSquareArea(bottomLeft, topRight))


    def test_2(self):
        s = Solution()
        bottomLeft = [[1,1],[2,2],[1,2]]
        topRight = [[3,3],[4,4],[3,4]]
        expected_result = 1
        self.assertEqual(expected_result, s.largestSquareArea(bottomLeft, topRight))


    def test_3(self):
        s = Solution()
        bottomLeft = [[1,1],[3,3],[3,1]]
        topRight = [[2,2],[4,4],[4,2]]
        expected_result = 0
        self.assertEqual(expected_result, s.largestSquareArea(bottomLeft, topRight))
       

try:
    unittest.main()
except SystemExit:
    None







