import unittest

from min_operations_to_write_y import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        grid = [[1,2,2],[1,1,0],[0,1,0]]
        expected_result = 3
        self.assertEqual(expected_result, s.minimumOperationsToWriteY(grid))

    def test_2(self):
        s = Solution()
        grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]
        expected_result = 12
        self.assertEqual(expected_result, s.minimumOperationsToWriteY(grid))

       

try:
    unittest.main()
except SystemExit:
    None











