import unittest
from number_of_adjacent_elements_with_the_same_color import Solution


class TestSolution(unittest.TestCase):


    def test_1(self):
        n = 4
        queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
        s = Solution()
        result = s.colorTheArray(n, queries)
        self.assertEqual([0,1,1,0,2], result)

    def test_2(self):
        n = 1
        queries = [[0,100000]]
        s = Solution()
        result = s.colorTheArray(n, queries)
        self.assertEqual([0], result)


try:
    unittest.main()
except SystemExit:
    None


















