import unittest


from node_with_highest_edge_score import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        edges = [1,0,0,0,0,7,7,5]
        output = 7
        self.assertEqual(output, s.edgeScore(edges))

    def test_2(self):
        s = Solution()
        edges = [2,0,0,2]   
        output = 0
        self.assertEqual(output, s.edgeScore(edges))


try:
    unittest.main()
except SystemExit:
    None
