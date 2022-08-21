import unittest


from largest_local_values_in_a_matrix import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
        output = [[9,9],[8,6]]
        self.assertEqual(output, s.largestLocal(grid))

    def test_2(self):
        s = Solution()
        grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
        output = [[2,2,2],[2,2,2],[2,2,2]]
        self.assertEqual(output, s.largestLocal(grid))

try:
    unittest.main()
except SystemExit:
    None
