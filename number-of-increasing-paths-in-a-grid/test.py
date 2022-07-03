import unittest
from number_of_increasing_paths_in_a_grid import Solution





class TestSolution(unittest.TestCase):


    def test_0(self):
        s = Solution()
        result = s.countPaths([[1,1],[3,4]])
        self.assertEqual(result, 8)

    def test_1(self):
        s = Solution()
        result = s.countPaths([[1],[2]])
        self.assertEqual(result, 3)
try:
    unittest.main()
except SystemExit:
    None