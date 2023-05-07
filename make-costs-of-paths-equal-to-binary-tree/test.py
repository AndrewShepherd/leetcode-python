import unittest
from make_costs_of_paths_equal_to_binary_tree import Solution


class TestSolution(unittest.TestCase):


    def test_1(self):
        n = 7
        cost = [1,5,2,2,3,3,1]
        s = Solution()
        result = s.minIncrements(n, cost)
        self.assertEqual(6, result)

    def test_0(self):
        n = 3
        cost = [5,3,3]
        s = Solution()
        result = s.minIncrements(n, cost)
        self.assertEqual(0, result)

    def test_3(self):
        n = 3
        cost = [5,3,3]
        s = Solution()
        result = s.minIncrements(n, cost)
        self.assertEqual(0, result)


try:
    unittest.main()
except SystemExit:
    None



















