
import unittest
from reachable_nodes_with_restrictions import Solution




class TestSolution(unittest.TestCase):


    def test_0(self):
        s = Solution()
        result = s.reachableNodes(7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4,5])
        self.assertEqual(4, result)

    def test_1(self):
        s = Solution()
        result = s.reachableNodes(7, [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], [4,2,1])
        self.assertEqual(3, result)

try:
    unittest.main()
except SystemExit:
    None